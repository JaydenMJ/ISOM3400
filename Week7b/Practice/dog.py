
class Dog():
    def __init__(self, name, chases_cats):
        self.name = name
        self.chases_cats = chases_cats
        
    def getName(self):
        return self.name
    
    def chasesCats(self):
        return self.chases_cats
    
    def __str__(self):
        return f"{self.name} is a Dog."

if __name__ =="__main__":
    dog = Dog("Cash", "chasing .....cats")
    print(dog)
    print(dog.chasesCats())
    print(f'My dog is {dog.getName()}')