class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, \
                 guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = self.set_meat(meat)
        self.to_go = self.set_to_go(to_go)
        self.rice = self.set_rice(rice)
        self.beans = self.set_beans(beans)
        self.extra_meat = self.set_extra_meat(extra_meat)
        self.guacamole = self.set_guacamole(guacamole)
        self.cheese = self.set_cheese(cheese)
        self.pico = self.set_pico(pico)
        self.corn = self.set_corn(corn)
        
#Setters and getters
    def set_meat(self, choice):
        if choice in ['chicken', 'pork', 'steak', 'tofu']:
            self.meat = choice
        else:
            self.meat = False
        return self.meat

    def get_meat(self):
       return self.meat
#
    def set_to_go(self, choice):
        if choice in [True, False]:
            self.to_go = choice
        else:
            self.to_go = False
        return self.to_go
    
    def get_to_go(self):
        return self.to_go    
#    
    def set_rice(self, choice):
        if choice in ['brown', 'white']:
            self.rice = choice
        else:
            self.rice = False
        return self.rice

    def get_rice(self):
        return self.rice
#    
    def set_beans(self, choice):
        if choice in ['black', 'pinto']:
            self.beans = choice
        else:
            self.beans = False
        return self.beans
    
    def get_beans(self):
        return self.beans
#    
    def set_extra_meat(self, choice):
        if choice in [True, False]:
            self.extra_meat = choice
        else:
            self.extra_meat = False
        return self.extra_meat

    def get_extra_meat(self):
        return self.extra_meat
#    
    def set_guacamole(self, choice):
        if choice in [True, False]:
            self.guacamole = choice
        else:
            self.guacamole = False
        return self.guacamole
    
    def get_guacamole(self):
        return self.guacamole
#    
    def set_cheese(self, choice):
        if choice in [True, False]:
            self.cheese = choice
        else:
            self.cheese = False
        return self.cheese
   
    def get_cheese(self):
        return self.cheese
#
    def set_pico(self, choice):
        if choice in [True, False]:
            self.pico = choice
        else:
            self.pico = False
        return self.pico

    def get_pico(self):
        return self.pico
#    
    def set_corn(self, choice):
        if choice in [True, False]:
            self.corn = choice
        else:
            self.corn = False
        return self.corn
    
    def get_corn(self):
        return self.corn

#Function to calculate cost
    def get_cost(self):
        total = 5
        
        if self.meat in ['chicken', 'pork', 'tofu']:
            total += 1
        elif self.meat == 'steak':
            total += 1.5
            
        if self.extra_meat and self.meat != False:
            total += 1
            
        if self.guacamole:
            total += 0.75
            
        return total

#Test
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())
