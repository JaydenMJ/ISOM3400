

# %%

# Test while

# Example 1
i = 1
while i < 3:
    print(i ** 2)
    i = i+1
print('Bye')


#%%

# Example 2
# Endless loop

import time 

i = 1
while True:
    print(f"Hello x{i}")
    time.sleep(1)
    i += 1
    if i == 5:
        break
print("End of an endless loop")
#%%

# While else
# (WITHOUT break)
print('WITHOUT break')
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop (WITHOUT break): done.')
    
# (WITH break)
print('WITH break')
n = 5
while n > 0:
    n -= 1
    print(n)
    break
else:
    print('Loop (WITH break): done.')


#%%

# Example 4
courses=['ISOM3230','ISOM4100','ISOM3400','ISOM5240']
searching = [3230,1973,2000]

idx = 0
search_term = str(searching[idx])
while(search_term in courses[idx] and idx < len(courses)):
    print('The course code is', courses[idx], 'Found!')
    idx = idx + 1
print("Done!")

#%%
courses=['ISOM3230','ISOM4100','ISOM3400','ISOM5240']
searching = [3230,1973,2000]

idx = 0
search_term = str(searching[idx])
print(search_term)



# %%
def abc():
    print("a")
abc()
end= abc
# %%
