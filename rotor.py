import encoding 
import random

class Rotor:
    def __init__(self, forwardWiring = None, rotorPos = None, ringPos = None, notchPos = None):
        if forwardWiring is None:
            self.randomSubstitution()
        else:
            self.forwardWiring = forwardWiring
            # Create backward wiring by inverting the dictionary:
            self.backwardWiring = {v: k for k, v in forwardWiring.items()}

        if rotorPos is not None:
            self.rotorPos = rotorPos % 32
        else:
            self.rotorPos = 0
        
        if ringPos is not None:
            self.ringPos = ringPos % 32
        else:
            self.ringPos = 0 

        if notchPos:
            self.notchPos = notchPos % 32
        else:
            self.notchPos = 0

    def setRandomPos(self):
        self.rotorPos = random.randint(0,31)

    #back the backward wiring the inverse of the forward wiring
    def syncWiring(self):
        self.backwardWiring = {v: k for k, v in self.forwardWiring.items()}

    #create a random substitution cipher
    def randomSubstitution(self):
        self.forwardWiring = {} 
        self.backwardWiring = {} 
        perm = list(range(32))
        random.shuffle(perm)
        for i in range(32):
            c1 = encoding.num_to_char(i)
            c2 = encoding.num_to_char(perm[i])
            self.forwardWiring[c1] = c2
            self.backwardWiring[c2] = c1

    #forward pass of the encryption
    def forward(self, c: str) -> str:
        assert len(c) == 1
        shift = self.rotorPos - self.ringPos 

        c1 = encoding.shift_char_by_delta(shift, c)
        c2 = self.forwardWiring[c1]
        c3 = encoding.unshift_char_by_delta(shift, c2)
        return c3

    #backward pass of the encryption
    def backward(self, c: str) -> str: 
        assert len(c) == 1
        shift = self.rotorPos - self.ringPos 

        c1 = encoding.shift_char_by_delta(shift, c)
        c2 = self.backwardWiring[c1]
        c3 = encoding.unshift_char_by_delta(shift, c2)
        return c3

    
    def isAtNotch(self) -> bool:
        return self.notchPos == self.rotorPos

    #rotate the rotor by one
    def rotate(self):
        self.rotorPos = (self.rotorPos + 1) % 32

    def print(self):
        s = ""
        s += (" forward wiring = " + str(self.forwardWiring) + "\n")
        s += (" rotor pos = " + str(self.rotorPos)+ "\n")
        s += (" ring pos = " + str(self.ringPos)+ "\n")
        s += (" notchPos = " + str(self.notchPos)+ "\n")
        return s

    

