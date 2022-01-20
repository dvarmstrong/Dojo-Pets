#  Create the Pet Object



class Pet:

    def __init__(self, name, type, health, energy):
        
        self.name = name
        self.type = type 
        self.health = health
        self.energy = energy


    # Method to sleep and increase energy by 25 
    
    def eat(self):
        self.energy += 5 
        self.health += 10 
        return self 
    
    def play(self):
        self.health += 5 
        return self 
    
    def sleep(self):
        self.energy += 25 
        return self 

    def noise(self, sound):
        print(f'{self.name} says {sound}')
        return self
    
    def tricks(self, tricks):
        print(f"{self.name} can {tricks}")
        return self

# bubba = Pet("bubba","dog", "health", "energy")

# # bubba.noise("bark")
# # bubba.sleep().eat().play()
# # print(bubba.energy)
# # print(bubba.health)
# bubba.tricks("sit").noise("barks")




