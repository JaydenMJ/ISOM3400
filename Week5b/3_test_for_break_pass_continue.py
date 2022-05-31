
# %%

# For, If, break

for letter in 'HKUST':
    print('Current letter :', letter)
    if letter == 'K':        
        break

# %%

# For, If, break
# .lower()

for letter in 'HKUST'.lower():
    print('Current letter :', letter)
    if letter == 'k':        
        break

for letter in 'HKUST'.lower():
    print('Current letter :', letter)
    if letter.upper() == 'K':
        break

# %%

# For, pass
# Tell you the last one of T, shows already gone through there character 
for letter in 'HKUST'.lower():
    pass

print('Current letter :', letter)

#%%

# continue is used to skip the current block, 
# and return to the "for" or "while" statement.


# For, continue (WITHOUT continue)
for i in range(5):
    if i>2:
        print("Ignored",i)
        # continue
        # the following statement will be 
        # skipped if i > 2
        print("Processed",i)

# %%

# For, continue (WITH continue)
for i in range(5):
    if i>2:
        print("Ignored",i)
        continue
        # the following statement will be 
        # skipped if i > 2
        print("Processed",i)

# %%
