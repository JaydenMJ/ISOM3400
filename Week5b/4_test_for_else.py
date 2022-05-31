

#%%

# The else block just after for/while is 
# executed only when the loop is NOT 
# terminated by a break statement.


#%%


# Example 1: For and Else (without break)

for i in range(1, 4): 
    print(i) 
else:  # Executed because no break in for 
    print("No Break") 


#%%

# Example 2: For and Else (with break)

for i in range(1, 4): 
    print(i) 
    break
else: # Not executed as there is a break 
    print("No Break")
    
#%%

# Example 3: def, for, if

def contains_even_number(l): 
    for ele in l: 
        if ele % 2 == 0: 
            print ("list contains an even number") 
            break
  
    # This else executes only if break is NEVER 
    # reached and loop terminated after all iterations. 
    else:      
        print ("list does not contain an even number") 
  
# Driver code 
print ("For List 1:") 
contains_even_number([1, 9, 8]) 
print (" \nFor List 2:") 
contains_even_number([1, 3, 5]) 

# %%
