
from GradingBot_V2 import GradingBot

class GradingISOM3400(GradingBot):
    
    def __init__(self,courseCode,instructor):
        GradingBot.__init__(self,courseCode)
        self.instructor=instructor

    def __str__(self):
        return f"Course: {self.courseCode}\nInstructor:{self.instructor}"

gradeJames=GradingISOM3400("ISOM3200","James")

print(gradeJames)
gradeJames.show_info()
#ver1
# class GradingBot(object):
#     def __init__(self):
#         print("Bot!!")
    
#     def __del__(self):
#         pass
    
#     def __str__(self):
#         return "I am a Grading bot."

# obj1 = GradingBot()
# print(obj1)


#ver2

# from GradingBot import GradingBot


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

