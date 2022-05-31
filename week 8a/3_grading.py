from GradingBot_V2 import GradingBot

class GradingISOM3400(GradingBot):
    def __init__(self,courseCode,instructor):
        GradingBot.__init__(self,courseCode)
        self.instructor=instructor
    def __str__(self):
        return f"{self.courseCode}{self.instructor}"

    def __del__(self):
        pass

if __name__ =='__main__':
    grader_james=GradingISOM3400("ISOM3400","James")
    print(grader_james)
    grader_james.show_info()
# # %%
# #ver2

# from GradingBot_v2 import GradingBot

# class GradingISOM3400(GradingBot):
#     def __init__(self, courseCode, instructor):
#         GradingBot.__init__(self, courseCode)
#         self.instructor = instructor
    
#     def __str__(self):
#         return f"Course: {self.courseCode}\nInstructor: {self.instructor}"    

#     def __del__(self):
#         pass
    


# grader_James = GradingISOM3400("ISOM3400", "James Kwok")
# print(grader_James)
# # %%
