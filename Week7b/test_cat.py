
from pets import Pet

class Cat(Pet):
    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs

    def __str__(self):
        return f"{self.name} is a lovely cat"

if __name__ == '__main__':
    cat1 = Cat("Kitty1", "hates cats")
    print(cat1)
    print(cat1.getName(), cat1.hatesDogs())
    print(f'My cat is {cat1.getName()}')

cat2 = Cat("Kitty2", "hates dogs")
print(cat2)
print(cat2.getName(), cat2.hatesDogs())
print(f'My cat is {cat2.getName()}')
    