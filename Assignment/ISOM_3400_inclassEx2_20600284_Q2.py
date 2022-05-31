from Q2_given_class import MyCourse

class BBACourse(MyCourse):
    def __init__(self,CourseCode,CourseTitle,Teacher):
        MyCourse.__init__(self,CourseCode,CourseTitle)

    def __str__(self):
        return "This is a BBA Course"

if __name__ =="__main__":
    course2= BBACourse("ISOM3400","Python","James")
    course2.showinfo()
    print(course2)