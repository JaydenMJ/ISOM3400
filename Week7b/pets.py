

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


if __name__ == '__main__':
    cat = Pet("Kitty", "Cat")
    print(cat)
