
class BBAIS_student(object):               
    title = "Mr/Miss"
    
    # contructor
    def __init__(self, fname, lname):   
        self.last_name = lname     
        self.first_name = fname    
        

    def show_info(self):
        print(self.title, 
              self.first_name, 
              self.last_name)


    # destructor
    def __del__(self):
        print("Died")

student_dict={}

stu1=BBAIS_student("james","kwok")
stu1.last_name= "ISOM"      #Diectly change outside the class
student_dict["student1"]=stu1

stu2= BBAIS_student("George","Clooney")
student_dict["student2"]= stu2

for student in student_dict:
    student_dict[student].show_info()
    