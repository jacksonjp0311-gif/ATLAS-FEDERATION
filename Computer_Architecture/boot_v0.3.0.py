"""ATLAS FORGE Computer Architecture v0.3: deterministic educational boot images.

The header/checksums prove *byte consistency*, not origin, signature, chip identity,
physical power-failure atomicity, or any security against a malicious image author.
Keeps AT8 ISA unchanged (two bytes/instruction, 2..256 byte ROM).
"""
from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha256
import struct,zlib
from .isa import validate_rom
from .v02_ecc import protect_rom,recover_rom

MAGIC=b'AT8R'
IMAGE_VERSION=3
HEADER=struct.Struct('>4sBBHI32s')
MAX_GENERATION=2**32-1

class BootIntegrityError(ValueError):pass


def encode_boot_image(rom:bytes)->bytes:
    validate_rom(rom)
    return HEADER.pack(MAGIC,IMAGE_VERSION,0,len(rom),zlib.crc32(rom),sha256(rom).digest())+rom


def decode_boot_image(blob:bytes):
    if type(blob) is not bytes or len(blob)<HEADER.size+2:raise BootIntegrityError('missing or nonbinary boot image')
    magic,version,flags,count,crc,digest=HEADER.unpack(blob[:HEADER.size])
    if magic!=MAGIC or version!=IMAGE_VERSION or flags!=0:
        raise BootIntegrityError('unknown boot header, version or reserved flags')
    if count<2 or count>256 or count%2 or len(blob)!=HEADER.size+count:
        raise BootIntegrityError('truncated, oversized, or misaligned ROM payload')
    rom=blob[HEADER.size:]
    if zlib.crc32(rom)!=crc or sha256(rom).digest()!=digest:
        raise BootIntegrityError('payload failed CRC32 or SHA-256 integrity')
    try:validate_rom(rom)
    except ValueError as exc:raise BootIntegrityError('image contains invalid AT8 ROM') from exc
    return {'rom':rom,'rom_sha256':digest.hex(),'image_sha256':sha256(blob).hexdigest(),
            'format_version':version,'sha256_is_authentication':False,
            'rom_bytes':count}


def ecc_encode_image_payload(image:bytes):
    parsed=decode_boot_image(image)
    return protect_rom(parsed['rom'])


def ecc_recover_image_payload(encoded,expected_image:bytes):
    parsed=decode_boot_image(expected_image)
    try:recovered=recover_rom(encoded,parsed['rom_sha256'])
    except (ValueError,TypeError) as exc:raise BootIntegrityError('ROM ECC recovery failed') from exc
    if recovered['rom']!=parsed['rom']:
        raise BootIntegrityError('recovered ROM does not match exact boot image')
    return {'rom':recovered['rom'],'corrected_words':recovered['corrected_words'],
            'rom_sha256':recovered['rom_sha256'],
            'recovery_authorized_by_external_signature':False}


@dataclass(frozen=True)
class BootSlot:
    generation:int
    image:bytes
    committed:bool
    def __post_init__(self):
        if type(self.generation) is not int or not 0<=self.generation<=MAX_GENERATION:
            raise ValueError('generation must be uint32')
        if type(self.image) is not bytes or type(self.committed) is not bool:
            raise ValueError('slot requires exact bytes and Boolean commit')


def select_boot_slot(slot_a:BootSlot|None,slot_b:BootSlot|None):
    states={'A':slot_a,'B':slot_b};valid=[];rejected=[]
    for name,slot in states.items():
        if slot is None:rejected.append({'slot':name,'reason':'empty'});continue
        if type(slot) is not BootSlot:raise ValueError('invalid slot type')
        if not slot.committed:rejected.append({'slot':name,'reason':'not_committed'});continue
        try:parsed=decode_boot_image(slot.image)
        except BootIntegrityError:rejected.append({'slot':name,'reason':'invalid_image'});continue
        valid.append((slot.generation,name,parsed))
    if not valid:raise BootIntegrityError('no committed, checksum-valid image')
    valid.sort(reverse=True)
    if len(valid)>1 and valid[0][0]==valid[1][0] and valid[0][2]['rom_sha256']!=valid[1][2]['rom_sha256']:
        raise BootIntegrityError('equal-generation images conflict: fail closed')
    chosen=valid[0]
    return {'selected_slot':chosen[1],'generation':chosen[0],
            'image_sha256':chosen[2]['image_sha256'],'rom_sha256':chosen[2]['rom_sha256'],
            'rom':chosen[2]['rom'],'rejected':tuple(rejected),
            'physical_power_loss_atomicity_demonstrated':False}


def stage_update(slot_a:BootSlot|None,slot_b:BootSlot|None,rom:bytes,
                 generation:int,interrupt_at:str='none'):
    """Simulation: before_data -> after_data -> after_commit; not physical flash writes."""
    if interrupt_at not in ('none','before_data','after_data','after_commit'):
        raise ValueError('unknown interruption stage')
    if type(generation) is not int or not 0<=generation<=MAX_GENERATION:
        raise ValueError('generation must be uint32')
    states={'A':slot_a,'B':slot_b}
    try:current=select_boot_slot(slot_a,slot_b)
    except BootIntegrityError:current=None
    if current is not None and generation<=current['generation']:
        raise ValueError('new generation must be greater than selected committed generation')
    target='B' if current and current['selected_slot']=='A' else 'A'
    if interrupt_at=='before_data':return slot_a,slot_b
    image=encode_boot_image(rom)
    states[target]=BootSlot(generation,image,committed=interrupt_at in ('none','after_commit'))
    return states['A'],states['B']
