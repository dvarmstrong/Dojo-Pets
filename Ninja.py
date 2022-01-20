# Creating a Ninja class

from Pets import Pet
# from modularizing.Dojo_and_Pets.Pets import Pet


class Ninja:
    def __init__(self,firstName, lastName, pet, treats, petFood):
        
        self.firsName = firstName
        self.lastName = lastName
        self.pet = pet
        self.treats = treats
        self.petFood = petFood
    

    def walk(self):
        self.pet.play()
        return self
            

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self


bubba = Pet("bubba", "dog", 20, 20)

kenny = Ninja("kenny","loggins", bubba, "cookies", "meat" )

print(kenny.pet.name)

kenny.walk()
kenny.feed()
print(kenny.pet.energy)