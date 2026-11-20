"""Run bounded AT8 demonstration via the original standalone reference library."""
from .programs import examples
from .spec import SpecMachine
from .microcoded import MicrocodedMachine

def main():
    for name,rom in examples().items():
        tape={1:[7]} if name=='input_output' else {}
        s=SpecMachine(rom,tape);m=MicrocodedMachine(rom,tape)
        sr=s.run(max_steps=100);mr=m.run(max_instructions=100)
        if not(sr['halted'] and mr['halted'] and sr['snapshot']==mr['snapshot']):
            raise AssertionError('independent implementations diverged')
        print(name,'steps=',sr['steps'],'outputs=',sr['snapshot']['output'],
              'ram0=',sr['snapshot']['ram'][0],'acc=',sr['snapshot']['regs'][0])
    print('ATLAS FORGE / AT8 computer architecture: software reconstruction only; no physical device demonstrated.')

if __name__=='__main__':main()
