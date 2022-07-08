#Sometimes, when studing math, I like to also practice programming skills by writing code.

#Classes
class fraction:
    
    def __init__(self, nominator, denominator):
        self.nom = nominator
        self.denom = denominator
        self.hdivisor = self.hdivisor()
        
    def hdivisor(self):
        self.hdivisor = 'No common divisor'
      
        for i in range(min(self.nom, self.denom), 1, -1):
            if (self.nom % i == 0) and (self.denom % i == 0):
                self.hdivisor = i
                break
             
        return self.hdivisor

    def reduction(self):
        return self.nom // self.hdivisor, self.denom // self.hdivisor    

x = fraction(1233, 9990)     

print(x.hdivisor)
print(x.reduction())     
