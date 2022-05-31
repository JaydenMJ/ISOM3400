
class GradingBot(object):
    def __init__(self):
        pass

    def __del__(self):
        pass
    
    def show_info(self):
        print("[Info]: Nothing")

    def __str__(self):
        return "I am Superclass"

if __name__ == "__main__":
    obj1=GradingBot()
    obj1.show_info()
    print(obj1)

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