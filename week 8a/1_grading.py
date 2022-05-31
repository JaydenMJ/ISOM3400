
class GradingBot(object):
    pass

    def __init__(self):
        pass

    def __del__(self):
        pass

    def show_info(self):
        print("[Info]:I am Superclass")

    def __str__(self):
        return "[Object]:I am Superclass"

# ==== Main Program

obj1=GradingBot()
obj1.show_info()
print(obj1)


# #%%
# #ver1
# class GradingBot(object):
#     def __init__(self):
#         print("Bot!!")
    
#     def __del__(self):
#         pass
    
#     def __str__(self):
#         return "I am a Grading bot."

# obj1 = GradingBot()
# print(obj1)

# # %%
# #ver2

# class GradingISOM3400(GradingBot):
#     def __init__(self):
#         GradingBot.__init__(self)
#         print('I am the child')
    
#     def __del__(self):
#         pass
    
#     def __str__(self):
#         return "I am ISOM3400 grading bot."    


# grader_James = GradingISOM3400()
# print(grader_James)
# # %%
