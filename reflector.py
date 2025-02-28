import random
import encoding

class Reflector:
    def __init__(self):
        self.wiring = {}
        for i in range(16):
            self.wiring[encoding.num_to_char(i)] = encoding.num_to_char(31-i) 
            self.wiring[encoding.num_to_char(31-i)] = encoding.num_to_char(i)
    
    def forward(self, c: str):
        assert len(c) == 1
        return self.wiring[c] 
    
    def printWiring(self):
        print(self.wiring)
