
#%%
# Try Except: Example 1

try:
    print(ISOM)    # ISOM is NOT defined, an error occurs
except:
    print("An exception occurred")

#%%

# Try Except: Example 2 - TWO except

try:
    print(ISOM)    # This is called "NameError"
except NameError:
    print("Variable ISOM is not defined")
except:
    print("Other errors")

# %%

# Try Except: Example 3 - except and else

try:
    print("ISOM")
except:
    print("An error is found")
else:  # Execute this when No Error is found
    print("No error is found")
# %%

# Try Except: Example 4 - except and finally

try:
    print("ISOM")
except:
    print("An error is found")
finally: # Execute regardless of error
    print("The 'try except' is finished")


# %%
