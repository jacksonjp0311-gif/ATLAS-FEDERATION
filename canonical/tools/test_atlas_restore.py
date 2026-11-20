"""Offline split-volume full Atlas restoration contract tests on small synthetic ZIPs."""
import importlib.util,hashlib,json,pathlib,tempfile,unittest,zipfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('atlas_full_restore',ROOT/'SURVIVAL/RESTORE_FULL_ATLAS.py')
restore=importlib.util.module_from_spec(sp);sp.loader.exec_module(restore)

class TestFullRecovery(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=pathlib.Path(self.tmp.name)
        self.parts=self.root/'parts';self.parts.mkdir()
        self.input=self.root/'full.zip'
        self.filename='ATLAS_COLLECTION_Computer_Architecture_v0.5.0.zip'
        with zipfile.ZipFile(self.input,'w') as z:
            z.writestr('ATLAS_COLLECTION_Computer_Architecture_v0.5.0/README.txt','SURVIVE THE TRANSPORT')
        blob=self.input.read_bytes();self.partslist=[]
        for idx,start in enumerate(range(0,len(blob),40),1):
            raw=blob[start:start+40];name=f'{self.filename}.part{idx:03d}'
            (self.parts/name).write_bytes(raw)
            self.partslist.append({'filename':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
        self.meta={'schema':'atlas.full-archive-volume-manifest/1','full_archive_filename':self.filename,
             'full_archive_bytes':len(blob),'full_archive_sha256':hashlib.sha256(blob).hexdigest(),
             'zip_members':1,'root_directory':'ATLAS_COLLECTION_Computer_Architecture_v0.5.0',
             'parts':self.partslist}
        self.manifest=self.root/'manifest.json';self.update()
    def tearDown(self):self.tmp.cleanup()
    def update(self):self.manifest.write_text(json.dumps(self.meta))
    def test_roundtrip(self):
        out=self.root/'restored.zip';res=restore.recover(self.parts,self.manifest,out)
        self.assertEqual(out.read_bytes(),self.input.read_bytes());self.assertEqual(res['result'],'passed')
    def test_refuse_preexisting_output(self):
        with self.assertRaises(ValueError):restore.recover(self.parts,self.manifest,self.input)
    def test_corrupt_volume(self):
        p=self.parts/self.partslist[0]['filename'];p.write_bytes(b'Z'+p.read_bytes()[1:])
        with self.assertRaises(ValueError):restore.recover(self.parts,self.manifest,self.root/'out.zip')
    def test_missing_part(self):
        (self.parts/self.partslist[-1]['filename']).unlink()
        with self.assertRaises(ValueError):restore.recover(self.parts,self.manifest,self.root/'out.zip')
    def test_wrong_size(self):
        self.meta['parts'][0]['bytes']+=1;self.update()
        with self.assertRaises(ValueError):restore.recover(self.parts,self.manifest,self.root/'out.zip')
    def test_reordered(self):
        self.meta['parts'].reverse();self.update()
        with self.assertRaises(ValueError):restore.recover(self.parts,self.manifest,self.root/'out.zip')
    def test_path_traversal_name(self):
        self.meta['parts'][0]['filename']='../evil.part000';self.update()
        with self.assertRaises(ValueError):restore.recover(self.parts,self.manifest,self.root/'out.zip')
    def test_wrong_full_digest(self):
        self.meta['full_archive_sha256']='0'*64;self.update()
        with self.assertRaises(ValueError):restore.recover(self.parts,self.manifest,self.root/'out.zip')
    def test_duplicate_manifest_key(self):
        self.manifest.write_text('{"schema":"atlas.full-archive-volume-manifest/1","schema":"bad"}')
        with self.assertRaises(ValueError):restore.recover(self.parts,self.manifest,self.root/'out.zip')
    def test_symlink_part(self):
        p=self.parts/self.partslist[0]['filename'];q=self.root/'real';q.write_bytes(p.read_bytes());p.unlink();p.symlink_to(q)
        with self.assertRaises(ValueError):restore.recover(self.parts,self.manifest,self.root/'out.zip')
    def test_zip_path_escape(self):
        with zipfile.ZipFile(self.input,'w') as z:z.writestr('../escape.txt','bad')
        blob=self.input.read_bytes()
        for p in self.parts.iterdir():p.unlink()
        self.meta['parts']=[]
        for idx,start in enumerate(range(0,len(blob),40),1):
            raw=blob[start:start+40];name=f'{self.filename}.part{idx:03d}'
            (self.parts/name).write_bytes(raw);self.meta['parts'].append({'filename':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
        self.meta['full_archive_bytes']=len(blob)
        self.meta['full_archive_sha256']=hashlib.sha256(blob).hexdigest()
        self.update()
        with self.assertRaises(ValueError):restore.recover(self.parts,self.manifest,self.root/'out.zip')
        self.assertFalse((self.root/'out.zip').exists())
    def test_full_zip_crc(self):
        self.assertEqual(restore.validate_name(self.partslist[0]['filename']),self.partslist[0]['filename'])
        with self.assertRaises(ValueError):restore.validate_name('arbitrary.zip')

if __name__=='__main__':unittest.main()
