

#%%
# Accessing Data using For-loop
# Lists

list_numbers = [1, 2, 3, 4, 5]
#comprehension

for num in list_numbers:
  print(type(num),num*2)
  square = num**2
  print(square)
  
#%%
# Accessing Data using For-loop
# Tuples


tuple_numbers = tuple(list_numbers)

for num in tuple_numbers:
  square = num**2
  print(square)


#%%
# Accessing Data using For-loop
# Dictionaries

# reference
# {"James":"Kwok", "ISOM":"1234", "Alex":123, 23:True}

dict_1 = {"James":"Kwok", 
          "ISOM":"1234", 
          "Alex":123, 
          23:True}

for key in dict_1:
    print("Key =",key)
#%% 
test3={23:0,25:0,47:1,52:0,46:1}
test4=tuple(test3)
test5={23:0,25:0,47:1,52:0,46:1}
#%%
for num in test3:
  print(num,test3[num])
#%%
for num in test4:
  print(num,test4)


#%%
listage=[22,25,47,52,46]
listbi=(0,0,1,0,1)

dict1={23:0,25:0,47:1,52:0,46:1}

for num in dict1:
  print(num,dict1[num])

# %%
