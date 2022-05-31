

# For Loop - list

#%%

# for loop with list

num_list = [0, 1, 2]

for x in num_list:
    print(f'for-loop: Number = {x}')

#%%
    
# Enumerate and zip

actor_list = ['Thomas Holland', 
              'Robert Downey', 
              'Benedict Cumberbatch']
hero_list = ['Spiderman', 
             'Iron Man',
             'Doctor Stange']

for idx, name in enumerate(actor_list):
    print(idx, name)

for actor, hero in zip(actor_list, hero_list):
    print(hero, "is", actor)



#%%

# prime number
primes = [1, 3, 5, 7, 11]

for prime in primes:
    print('Prime Number', prime)
    
# %%

# Nested For
# Processing sublist

world_univ = [['HKUST', 'HKU', 'CUHK'],
              ['NUS', 'NTU', 'SMU'],
              ['MIT', 'USC', 'NYU']]

for sublist in world_univ:
    for u_name in sublist:
        num_letter = len(u_name)
        print("The University: " + u_name + 
              " is " + str(num_letter) + 
              " characters long.")


# %%
world_univ = [['HKUST', 'HKU', 'CUHK'],
              ['NUS', 'NTU', 'SMU'],
              ['MIT', 'USC', 'NYU']]

print(len(world_univ))
# %%

list_1=[1,2,3,4,5,6]


print()
# %%
