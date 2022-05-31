
from pets import Pet

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

