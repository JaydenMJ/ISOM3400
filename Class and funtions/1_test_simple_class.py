
#%%
# Create a class
# Your first class

# This is an emply class
class ISOM:
    pass    # does nothing but required in this case

print(ISOM)

# ISOM is not the same as isom
# Captial letter is used for our own classes
# Lowercase names are used for built-in classes


# %%
# Create an object
class ISOM:
    pass
mydept = ISOM()       # mydept is an object
print(mydept)
print(type(mydept))

# %%
# Instance attributes
class ISOM:
    pass

mydept=ISOM()

mydept.course = "ISOM3400"
mydept.url = "http://www.bm.ust.hk/isom"
mydept.founding_year = 1995
mydept.is_top = True

print(mydept.course)
print(mydept.url)
# %%
class ISOM:
    pass

mydept=ISOM()

mydept.course = "ISOM3400"
mydept.url = "http://www.bm.ust.hk/isom"
mydept.founding_year = 1995
mydept.is_top = True
'''
print(mydept.course)
print(mydept.url)
print(mydept.founding_year)
print(mydept.is_top)
'''
dept2=ISOM()
dept2.course= "ISOM3230" # instantiate
print(dept2.__dict__)
print(mydept.__dict__)


# course, url, founding_year,and is_top are 
# attributes, not variables. More specifically, 
# they are instance attributes.

# Instance attributes need a dot for setting and 
# getting values of attributes.
# Variables do not need "dots".

# %%
# Create another object

another_dept = ISOM()
print(another_dept.course)   # Attribute does not exist

# %%
# Show all attributes (not recommended)
# But not recommend to use

print(mydept.__dict__)
print(another_dept.__dict__)


# %%
