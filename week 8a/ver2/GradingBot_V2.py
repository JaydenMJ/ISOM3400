class GradingBot(object):
    def __init__(self,courseCode):
        self.courseCode=courseCode


    def __del__(self):
        pass
    
    def show_info(self):
        print("[Info]: Nothing")

    def __str__(self):
        return f"{self.courseCode}"

if __name__ == "__main__":
    obj1=GradingBot("ISOM3400")
    obj1.show_info()
    print(obj1)



    
# class GradingBot(object):

#     def __init__(self,courseCode):
#         self.courseCode=courseCode

#     def __del__(self):
#         pass
    
#     def show_info(self):
#         print("[Info]: Nothing")

#     def __str__(self):
#         return f"Course: {self.courseCode }"

# if __name__ == "__main__":
#     obj1=GradingBot("ISOM3400")
#     obj1.show_info()
#     print(obj1)

# class GradingBot(object):
#     def __init__(self):
#         print("Bot!!")
    
#     def __del__(self):
#         pass
    
#     def __str__(self):
#         return "I am a Grading bot."

# if __name__ == '__main__':
#     obj1 = GradingBot()
#     print(obj1)