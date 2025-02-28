import random
import encoding

class Plugboard:
    def __init__(self, wiring = None):
        if wiring is None: 
            self.clearPlugs()
        else:
            self.wiring = wiring 

    def clearPlugs(self):
        self.wiring = {}
        for i in range(32):
            self.wiring[encoding.num_to_char(i)] = encoding.num_to_char(i)

    def forward(self, s):
        ans = ""
        for c in s:
            ans += self.wiring[c]
        return ans 
    
    def addRandomPlugs(self, k):
        numbers = random.sample(range(32), 2*k)
        i = 0 
        for i in range(0, 2*k, 2):
            ind1 = numbers[i]
            ind2 = numbers[i+1]
            c1 = encoding.num_to_char(ind1)
            c2 = encoding.num_to_char(ind2)
            self.wiring[c1] = c2
            self.wiring[c2] = c1

    def addPlug(self, c1, c2):
        if not(c1 in self.wiring and c2 in self.wiring):
            print("invalid characters")

        if self.wiring[c1] == c1 and self.wiring[c2] == c2:
                self.wiring[c1] = c2
                self.wiring[c2] = c1
        else:
            print("invalid plug")

            
    def printPlugs(self):
        print(self.wiring)


    

        
    
    


                
