


# %%

# built-in functions
# enumerate and zip

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

# built-in functions
# sorted

actor_list = ['Thomas Holland', 
              'Robert Downey', 
              'Benedict Cumberbatch']
print("\nWITHOUT sorted()")
for actor in actor_list:
    print(actor)

print("\nWITH sorted()")
for actor in sorted(actor_list):
    print(actor)

# %%

# built-in functions
# reversed

actor_list = ['Thomas Holland', 
              'Robert Downey', 
              'Benedict Cumberbatch']
print("\nWITHOUT reversed()")
for actor in actor_list:
    print(actor)

print("\nWITH reversed()")
for actor in reversed(actor_list):
    print(actor)
# %%

# built-in functions
# sorted + reversed

actor_list = ['Thomas Holland', 
              'Robert Downey', 
              'Benedict Cumberbatch']
print("\nWITHOUT sorted()")
for actor in actor_list:
    print(actor)

print("\nWITH sorted()")
for actor in sorted(actor_list):
    print(actor)
    
print("\nWITH sorted() + reversed")
for actor in sorted(actor_list, reverse=True):
    print(actor)


# %%
