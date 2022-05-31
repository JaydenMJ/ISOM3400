class BBAIS_student(object):
    title="Mr/Mrs"

    def __init__(self,fname,lname):
        self.first_name=fname
        self.last_name=lname
        pass
    def show_info(self):
        print(self.title,
            self.first_name,
            self.last_name)
    def __del__(self):
        print("Died")

student_dict={}
student_list=[]


stu1=BBAIS_student("James","Kwok")    
student_dict["student1"]=stu1

stu2=BBAIS_student("Goerge","Clooney")    
student_dict["student2"]=stu2

for name in student_dict:
    student_dict[name].show_info()
#Use for-loop

