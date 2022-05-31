
#%%

# Create a class
class BBAIS_student(object):               
# class names begin with a capitial letter
    title = "Mr/Miss"
    
    # contructor
    def __init__(self, fname, lname):      
        # firstname is a field (or property)
        self.last_name = lname     
        # lastname is a field (or property)
        self.first_name = fname    
        # field names are lowercase and 
        # separated by underscores

    def show_info(self):
        print(self.title, 
              self.first_name, 
              self.last_name)

    # destructor
    def __del__(self):
        print("Died")


#%%
if __name == "__main__"
# stu1 is an instance of BBAIS_student class
# stu1 is also an object
stu1 = BBAIS_student("James",'Kwok')

#%%

# mobile_phone is a variable created on the fly
stu1.mobile_phone = "12345678"   

stu1.show_info()
print(stu1.__dict__)

# %%

del stu1

# %%

# Create another object
stu2 = BBAIS_student("George", "Clooney")
stu2.show_info()
stu2.phone_number = '33333333'
print(stu2.phone_number)


# %%

# Delete an object attribute
del stu1.mobile_phone
print(stu1.__dict__)

# %%

# Delete an object
del stu1

# %%
