
class Pet(object):    
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Dog(Pet): 
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats


if __name__ == '__main__':
    mydog = Dog("Cash", "chasing .....cats")
    print(mydog)
    print(mydog.chasesCats())
    print(f"My dog is {mydog.getName()}")
    