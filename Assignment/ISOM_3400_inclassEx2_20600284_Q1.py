

class Course(object):
   
    def __init__(self,CourseCode,CourseTitle):
        self.CourseCode=CourseCode
        self.CourseTitle=CourseTitle
        pass
    def __del__(self):
        pass
    def __str__(self):
        return "This is a course"

course1=Course("ISOM3400","Python")
course1.instructor="James"
print(f"{course1.CourseCode} is about {course1.CourseTitle} by {course1.instructor}")
print(course1.__dict__)
