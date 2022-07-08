#Classes

class fraction:
    
    def __init__(self, nominator, denominator):
        self.nom = nominator
        self.denom = denominator
        self.hdivisor = self.hdivisor()
        if self.denom == 0:
            self.denom = 1
            print('Since denominator cannot be equal to 0, it has been changed to 1.')

    def hdivisor(self):
        self.hdivisor = 1
      
        for i in range(min(self.nom, self.denom), 1, -1):
            if (self.nom % i == 0) and (self.denom % i == 0):
                self.hdivisor = i
                break
             
        return self.hdivisor

    def reduction(self):
            return self.nom // self.hdivisor, self.denom // self.hdivisor


x = fraction(5324,63400)     

print(x.hdivisor)
print(x.reduction())   
    
    
       
