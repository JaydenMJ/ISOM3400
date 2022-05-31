#%%

res1=input("Hungry")
if res1=="yes":
    res2=input("Have")
    if res2=="yes":
        print("Go to restaurant")
    else:
        print("Buy")
else:
    print("Go to sleep")


# %%

yes_list=["yes","perfect","y"]
no_list=["no","n","nonono"]

hungry=input("Am i hungry?")

if hungry.lower() in yes_list:
    money=input("Do you have $125?")
    if money.lower() in yes_list:
        print("Go to restaurant")
    elif money.lower() in no_list:
        print("Buy a hamburger")


# %%
list_old=[1,2,3,4,5,6,7,8,9,10]
list_new=[]
for num in list_old:
    if num%2==0:
        list_new.append(0)
    elif num%3==0:
        list_new.append(1)
    else:
        list_new.append(num)
print(list_new)
# %%
list_old=[1,2,3,4,5,6,7,8,9,10]

new=[0 if num %2==0 else
    1 if num%3==0 else
    num  for num in list_old]

print(new)
# %%
