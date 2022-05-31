
class Cat():
    def __init__(self, name, hates_dogs):
        self.name = name
        self.hates_dogs = hates_dogs
    
    def getName(self):
        return self.name
    
    def hatesDogs(self):
        return self.hates_dogs

    def __str__(self):
        return f"{self.name} is a Cat."
    
if __name__ =="__main__":
    cat = Cat("Kitty", "hates dogs")
    print(cat)
    print(cat.hatesDogs())
    print(f'My cat is {cat.getName()}')




    