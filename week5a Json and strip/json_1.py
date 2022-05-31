#%%
width=44
def check_balance(account):
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Check Balance".center(width)))
    for key , value in account['charles']['balance'].items():
        value=str(key)+" " +str(value)
        print("## {} ".format(value),"##".rjust(width-len(value)+1))
    print("## {} ##".format("".center(width)))
    print("##################################################")
account = {
        "charles":{"password": "a",
                   "balance": {"USD": 10,
                                "HKD": 10000,
                               },
                                
                            },
        "samuel":{"password": "secret",
                   "balance": {"USD": 10000,
                                "HKD": 10,
                                "CNY": 50,
                               },
                                
                            },
        }
'''cu =input("E\n")
for i in account["charles"]['balance']:
   
    if cu in i:
        withdraw_amount=int(input("How much would you like to withdraw?\n")  )
        if int(withdraw_amount)<60000 and int(withdraw_amount)<=account['charles']['balance'][cu]:
                    
            account['charles']['balance'][cu]-=withdraw_amount
            print("##################################################")
            print("## {} ##".format("".center(width)))
            print("## {} ##".format("Withdrawn Sucessfully".center(width)))
            print("## {} ##".format("".center(width)))
            print("## {} ##".format("1. Check Balance".ljust(width)))
            print("## {} ##".format("2. Exit".ljust(width)))
            print("##################################################")
            check=input("Enter the option: ")
            if check=='1':
                check_balance(account)
            else:
                break    '''
i =input("Name\n")

if i in account:
    print(account['samuel']['balance'][''])

'''    
print(account['charles']['balance']['USD']+1)
print(account['charles']['balance']['USD'])
cur=input("Please choose your account: ")

if cur== '1':
    print(account['charles']['balance']['USD'])
elif cur=='2':
    print(account['charles']['balance']['HKD'])
elif cur==3:
    print(account['charles']['balance']['CNY'])   
'''

# %%