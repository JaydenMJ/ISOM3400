


#%%
# Lists, Tuples, and Dictionaries

list1 = [1,"2", False]
tuple1 = ("1", True, False)
dict1 = {"James":"Kwok", "ISOM":"5240", "Alex":123, 23:True}

print(type(list1))
print(type(tuple1))
print(type(dict1))
#%%
# Creation - list

list_1 = list((1, '2', False))
list_2 = [1, "2", False]

list_3 = list()     # create an empty list
list_3.append(1)
list_3.append('2')
list_3.append(False)


#%%
# Creation - tuple

#tuple_1 = tuple("1", True, False)   # Error
tuple_1 = tuple(("1", True, False))
tuple_2 = ("1", True, False)

tuple_3 = tuple()     # create an empty tuple
tuple_3.append("1")   # Error
tuple_3.append(True)  # Error
tuple_3.append(False) # Error

tuple_4 = 27,
print("index=0", tuple_4[0])
#print(tuple_4[1])   # Error


#%%
# Creation - from list to tuple
var1=1
var2=1+1
var3=str(3)
l1=[var1,var2,var3]



tuple_5 = tuple(l1)
print(tuple_5)
# Creation - from list to tuple
list_4 = [1,2,3]
tuple_7 = tuple(list_4)
print(type(tuple_7), tuple_7)

# Create a tuple from a String data
tuple_6 = tuple('Hello')
print(tuple_6)
print("index=0", tuple_6[0])


#%%
# Creation - from tuple to list

list_5 = list(tuple_7)
print(type(list_5), list_5)

#%%
# Creation - dictionary

# reference
#    {"James":"Kwok", "ISOM":"1234", "Alex":123, 23:True}


dict_1 = dict()
dict_1 = {}
dict_1["James"] = 'Kwok'    # key="James", value="Kwok"
dict_1["ISOM"] = '1234'     # key="ISOM", value="1234"
dict_1[23] = True           # key=23, value=True
dict_1["Alex"] = 123        # key="Alex", value=123

print(dict_1)

#%%
# Creation - dictionary (alternative)

dict2={}

# reference
#    {"James":"Kwok", "ISOM":"1234", "Alex":123, 23:True}
dict2["James"]="Kowk"
dict2["Isom"]= 3230
dict2["Isom"]= 3400
dict2[23]=111

print(dict2)

dict_2 = {"James":"Kwok", 
          "ISOM":"1234", 
          "Alex":123, 
          23:True}

print(dict_2)


# %%
