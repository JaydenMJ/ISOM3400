

#%%
# (Not a function) - Setup

# Version 1
# Functions and Methods

class ISOM:
    pass    

#Create an object
mydept = ISOM() 

#Create attributes and assign values
mydept.course = "ISOM3400"
mydept.url = "http://www.bm.ust.hk/isom"
mydept.founding_year = 1995
mydept.is_top = True

#%%
# Define a function and use the function


def isom_info(isom):
    print("Course =", isom.course)
    print("URL =", isom.url)
    print("Founding Year =", isom.founding_year)
    print("ISOM is", "the top" if isom.is_top else "very good")

isom_info(mydept)

# Source: https://stackoverflow.com/questions/11529273/how-to-condense-if-else-into-one-line-in-python


# %%

# Version 2
# Integrate a function in a class

class ISOM:
    def info(self):
        print("Course =", self.course)
        print("URL =", self.url)
        print("Founding Year =", self.founding_year)
        print("ISOM is", "the top" if self.is_top else "very good")

#Create an object
mydept = ISOM() 

#Create attributes and assign values
mydept.course = "ISOM3400"
mydept.url = "http://www.bm.ust.hk/isom"
mydept.founding_year = 1995
mydept.is_top = True

mydept.info()

# %%

# Version 3
# Initialize attributes within the class

class ISOM:
    def initialize(self, course, url, founding_year, is_top):
        self.course = course
        self.url = url
        self.founding_year = founding_year
        self.is_top = is_top
        
    def info(self):
        print("Course =", self.course)
        print("URL =", self.url)
        print("Founding Year =", self.founding_year)
        print("ISOM is", "the top" if self.is_top else "very good")

#Create an object
mydept = ISOM() 

#Create attributes and assign values
mydept.initialize("ISOM3400", "http://www.bm.ust.hk/isom", 
                  1995, True)
mydept.info()


#%%

# Version 3a
# Initialize attributes within the class

class ISOM:
    def initialize(self, a, b, c, d):
        self.course = a
        self.url = b
        self.founding_year = c
        self.is_top = d
        
    def info(self):
        print("Course =", self.course)
        print("URL =", self.url)
        print("Founding Year =", self.founding_year)
        print("ISOM is", "the top" if self.is_top else "very good")

#Create an object
mydept = ISOM() 

#Create attributes and assign values
mydept.initialize("ISOM3400", "http://www.bm.ust.hk/isom", 
                  1995, True)
mydept.info()


# %%

# Version 4
# Constructor

# Constructors are used to set up the attribute values.
# Avoid using print() and input() in constructors
# Use another function for print() and input() instead.


class ISOM:
    # Constuctor
    def __init__(self, course, url, founding_year, is_top):
        self.course = course
        self.url = url
        self.founding_year = founding_year
        self.is_top = is_top
        
    def info(self):
        print("Course =", self.course)
        print("URL =", self.url)
        print("Founding Year =", self.founding_year)
        print("ISOM is", "the top" if self.is_top else "very good")

#Create an object and initialize the attributes
mydept = ISOM("ISOM3400", "http://www.bm.ust.hk/isom", 1995, True) 

mydept.info()

# %%

# Version 5
# More functions

# change course to courses and courses is a list
    # a function to add a new course to the list
    # update info() to show the course list

class ISOM:
    # Constuctor
    def __init__(self, course, url, founding_year, is_top):
        self.courses = []
        self.courses.append(course)
        self.url = url
        self.founding_year = founding_year
        self.is_top = is_top
        
    def add_course(self, new_course):
        self.courses.append(new_course)
        
    def info(self):
        for course in self.courses:
            print("Course =", course)
        print("URL =", self.url)
        print("Founding Year =", self.founding_year)
        print("ISOM is", "the top" if self.is_top else "very good")

#Create an object and initialize the attributes
mydept = ISOM("ISOM3400", "http://www.bm.ust.hk/isom", 1995, True)

# Invoke the add_course() function 
mydept.add_course("ISOM3230")
# Invoke the info() function
mydept.info()

# %%

# Version 6
# Get a list using return

class ISOM:
    # Constuctor
    def __init__(self, course, url, founding_year, is_top):
        self.courses = []
        self.courses.append(course)
        self.url = url
        self.founding_year = founding_year
        self.is_top = is_top
        
    def add_course(self, new_course):
        self.courses.append(new_course)

    def get_courselist(self):
        return self.courses
        
    def info(self):
        for course in self.courses:
            print("Course =", course)
        print("URL =", self.url)
        print("Founding Year =", self.founding_year)
        print("ISOM is", "the top" if self.is_top else "very good")

    def __del__(self):
        print('....dying....')

#Create an object and initialize the attributes
mydept = ISOM("ISOM3400", "http://www.bm.ust.hk/isom", 1995, True)

# Invoke the add_course() function 
mydept.add_course("ISOM3230")

# Invoke the get_courselist() function
# Approach 1
new_course_list = mydept.get_courselist()
print(new_course_list)

# Approach 2
print(mydept.get_courselist())


# %%

# Version 7
# Destructor


# To kill an object or instance

class ISOM:
    # Constuctor
    def __init__(self, course, url, founding_year, is_top):
        self.courses = []
        self.courses.append(course)
        self.url = url
        self.founding_year = founding_year
        self.is_top = is_top
        
    def add_course(self, new_course):
        self.courses.append(new_course)
    
    def get_courselist(self):
        return self.courses    
    
    def info(self):
        for course in self.courses:
            print("Course =", course)
        print("URL =", self.url)
        print("Founding Year =", self.founding_year)
        print("ISOM is", "the top" if self.is_top else "very good")

    def __del__(self):
        print('....dying....')

#Create an object and initialize the attributes
mydept = ISOM("ISOM3400", "http://www.bm.ust.hk/isom", 1995, True)

# Invoke the add_course() function 
mydept.add_course("ISOM3230")

print("del")
del mydept

# %%
