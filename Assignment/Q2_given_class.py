


class MyCourse(object):
    def __init__(self, CourseCode, CourseTitle):
        self.CourseCode = CourseCode
        self.CourseTitle = CourseTitle
    
    def __del__(self):
        pass

    def showinfo(self):
        print(self.CourseCode)
    def __str__(self):
        return f"This is a course."    



