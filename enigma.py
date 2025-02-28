from plugboard import Plugboard
from reflector import Reflector
from rotor import Rotor
import encoding


class Enigma: 
    def __init__(self, plugboard = None, reflector = None, leftRotor = None, middleRotor = None, rightRotor = None): 
        self.plugboard = plugboard if plugboard is not None else Plugboard()
        self.reflector = reflector if reflector is not None else Reflector()
        self.leftRotor = leftRotor if leftRotor is not None else Rotor()
        self.middleRotor = middleRotor if middleRotor is not None else Rotor()
        self.rightRotor = rightRotor if rightRotor is not None else Rotor() 

    
    def rotate(self):
        # If the middle rotor is at notch, double-step: rotate both middle and left rotors.
        if self.middleRotor.isAtNotch():
            self.middleRotor.rotate()
            self.leftRotor.rotate()
        # Else if the right rotor is at notch, then rotate the middle rotor.
        elif self.rightRotor.isAtNotch():
            self.middleRotor.rotate()
        # Always rotate the right rotor.
        self.rightRotor.rotate()

    def encryptChar(self, c):
        self.rotate()
        assert len(c) == 1
        c1 = self.plugboard.forward(c)
        ###COMPLETE ME###
        c9 = self.plugboard.forward(c8)
        return c9 
    
    def encrypt(self, s):
        return "".join(self.encryptChar(c) for c in s)
        
    def printToFile(self, output_filename):
        with open(output_filename, 'w') as outfile:
            print("Reflector: " + str(enigmaMachine.reflector.wiring), file=outfile)
            print("\n", file = outfile)
            print("Left rotor: " + str(enigmaMachine.leftRotor.print()), file = outfile)
            print("Middle rotor: " + str(enigmaMachine.middleRotor.print()), file = outfile)
            print("Right rotor: " + str(enigmaMachine.rightRotor.print()), file = outfile)
            print("Plugboard: " + str(enigmaMachine.plugboard.wiring), file = outfile)
