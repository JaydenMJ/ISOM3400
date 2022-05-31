from animals import animal

class cat(animal):
    pass
    def __init__(self,name,color):
        animal.__init__(self,name,color)

    def meow(self):
        print("meow...meow")

if __name__=="__main__":
    mycat=cat("British shorthair","white")
    print(f"The name is {mycat.show_name()}, the color is {mycat.show_color()}")
    mycat.meow()
# from animals import animal


# class cat(animal):
#     def __init__(self, name, color):
#         animal.__init__(self, name, color)

#     def meow(self):
#         print("meow...moew")


# if __name__ == "__main__":
#     mycat = cat("british shorthair", "white")
#     print(f"The name of the cat is {mycat.show_name()} , the color is  {mycat.show_color()}")
#     mycat.meow()

 