#%%
class ISOM:

    def initialize(self,a,b,c,d):
        self.course = a
        self.url = b
        self.founding_year = c
        self.is_top = d

    def isom_info(self):
        print(self.course)
        print(self.url)
        print(self.founding_year)
        print(self.is_top)

    
#Main
#Create an object
dept1 = ISOM() 

#Create attributes and assign values
dept1.initialize("ISOM3400","http://www.bm.ust.hk/isom",1995,True)

dept1.isom_info()
# %%
class ISOM:
    #Constructor
    def __init__(self,a,b,c,d):
        self.course = a
        self.url = b
        self.founding_year = c
        self.is_top = d

    def isom_info(self):
        print(self.course)
        print(self.url)
        print(self.founding_year)
        print(self.is_top)

    
#Main
#Create an object
dept1 = ISOM("ISOM3400","http://www.bm.ust.hk/isom",1995,True) 
dept1.isom_info()

#Create attributes and assign values
#dept1.initialize("ISOM3400","http://www.bm.ust.hk/isom",1995,True)




dept2=ISOM("ISOM3230","http://www.bm.ust.hk/isom",2005,True)
dept2.isom_info()
# %%
