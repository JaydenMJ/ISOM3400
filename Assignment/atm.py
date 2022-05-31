# -*- coding: utf-8 -*-
"""
@course: ISOM3400 L1
@author: Man Chun Kit
@student_id: 20600284

"""

import getpass
import random
import logging
width = 44
login_tried = 0
login_tried_tempt = 0
endProgram = False


account = {
        "charles":{"password": "thisIsMyPassword",
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
                   
currency = {
            "USD" : {
                    "USD" : 1,
                    "HKD" : 7.831600,
                    "JPY" : 7.831600/0.074600,
                    "CNY" : 7.831600/1.103100,
                    "EUR" : 7.831600/8.769800,
                    },
            "HKD" : {
                    "USD" : 1/7.862800,
                    "HKD" : 1,
                    "JPY" : 1/0.074600,
                    "CNY" : 1/1.103100,
                    "EUR" : 1/8.769800,
                    },
            "JPY" : {
                    "USD" : 0.073740/7.862800,
                    "HKD" : 0.073740,
                    "JPY" : 1,
                    "CNY" : 0.073740/1.103100,
                    "EUR" : 0.073740/8.769800,
                    },
            "CNY" : {
                    "USD" : 1.088200/7.862800,
                    "HKD" : 1.088200,
                    "JPY" : 1.088200/0.074600,
                    "CNY" : 1,
                    "EUR" : 1.088200/8.769800,
                    },
            "EUR" : {
                    "USD" : 8.640000/7.862800,
                    "HKD" : 8.640000,
                    "JPY" : 8.640000/0.074600,
                    "CNY" : 8.640000/1.103100,
                    "EUR" : 1,
                    },
        }

captcha_list = ['heLL0', 'HoW', "R", "YoU?"]

### Task 2 balance checking function
def check_balance(account, login):
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Check Balance".center(width)))
    # To print out the balance using for-loop and adjust the position using len
    for key , value in account[login]['balance'].items():
        value=str(key)+" " +str(value)
        print("## {} ".format(value),"##".rjust(width-len(value)+1))
    print("## {} ##".format("".center(width)))
    print("##################################################")
    


    return False
         

# Task 3: Cash Withdrawal		  
def cash_withdrawal(account, login):
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Select your account".center(width)))
    # To enumerate starting with 1 and print out the currency account available, adjust using rjust
    #Fining the Width of # using len   
    for i,key in enumerate(account[login]['balance'].keys(),start=1):
        print("## {} {} ".format(i,key),"##".rjust(width-len(key)-1))

    print("## {} ##".format("".center(width)))
    print("##################################################")
    
    acc=input("Please choose your account: \n")

    try:
        # To check whether the type in acc is within the list of currency of the user, terminate when there arent
        if acc in account[login]['balance']:
            withdraw_amount=int(input("How much would you like to withdraw?\n")  )
            if int(withdraw_amount)<60000 and int(withdraw_amount)<=account[login]['balance'][acc]:

            # when the account withdrawn amount in the user's account, minus the value to update the remaining balance
            # Print out the sucess menu
            # Call the check_balance function when input 1, return false for any other keys (2)  
                            
                account[login]['balance'][acc]-=withdraw_amount
                print("##################################################")
                print("## {} ##".format("".center(width)))
                print("## {} ##".format("Withdrawn Sucessfully".center(width)))
                print("## {} ##".format("".center(width)))
                print("## {} ##".format("1. Check Balance".ljust(width)))
                print("## {} ##".format("2. Exit".ljust(width)))
                print("##################################################")
                check=input("Enter the option: ")

                if check=='1':
                    check_balance(account,login)
                else:
                    return False
            else:
                print("There is not enough money in the balance")
                return False   
        else:
            print("There is no ",acc," account in your card.")
            return False
    # Check for value error
    except ValueError:
        print("Please enter valid number(Integers Only)")
    return False

# Task 4: Transfer money to other user
def transfer(account, login):

    # Print out user menu for transfer function
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Select your account to transfer".center(width)))
    for ic,key in enumerate(account[login]['balance'].keys(),start=1):
        print("## {} {} ".format(ic,key),"##".rjust(width-len(key)-1))        
    print("## {} ##".format("".center(width)))
    print("##################################################")

    # If the input account is not in the account , terminate the program
    i=input("Please choose your account(In Letter): \n")
    if i not in account[login]['balance']:
        print("There is no ",i, "account in your account")
    else:
        # If the input accoint exist in the user account, do the following 
        # To check whether the receiver is recorded in the bank system, if no terminate

        transfer_account=input("Please enter the name of the receiver: \n")        
        if transfer_account not in account:
            print("The receiver was not founded!")
            return False
        else:
            # if the receiver is recored in the system, ask the user to choose the Currency account to transfer
            # Check whether the transfer exceeds 15000 and within the money of the login balance
            # If the transfer currency does not exist in that person;s account, ask the user to exchange the currency first then transfer
            acc_t=input("Please choose the receiver's transfer account(In Letter): \n")
            if acc_t in account[transfer_account]['balance'] and i==acc_t:
                
                
                transfer_amount=int(input("How much would you like to transfer?\n"))
                if transfer_amount>15000:
                    print("Transfer amount exist 15000")
                elif int(transfer_amount)<15000 and int(transfer_amount)<=account[login]['balance'][acc_t]:
                    account[login]['balance'][acc_t]-=transfer_amount
                    account[transfer_account]['balance'][acc_t]+=transfer_amount
                    print("##################################################")
                    print("## {} ##".format("".center(width)))
                    print("## {} ##".format("Transfer Sucessfully".center(width)))
                    print("## {} ##".format("".center(width)))
                    print("## {} ##".format("1. Check Balance".ljust(width)))
                    print("## {} ##".format("2. Exit".ljust(width)))
                    print("##################################################")
                    check=input("Enter the option: ")
                    if check=='1':
                        check_balance(account,login)
                    else:
                        return True   
                    
                else:
                    print("Not enough money")
                    exit
                    
            else:                    
                print("Please first exchange the currency before transfer to different currency account")
                return False
                
            return False

    return False            
    
                
	


# Task 5: Currency Exchange
# Print out the exchange menu
def currency_exchange(account, login):
    print("##################################################")
    print("## {} ##".format("".center(width)))
    print("## {} ##".format("Choice an account for currency exchange".center(width)))
    for ic,key in enumerate(account[login]['balance'].keys(),start=1):
        print("## {} {} ".format(ic,key),"##".rjust(width-len(key)-1))        
    print("## {} ##".format("".center(width)))
    print("##################################################")
    
# Check whether the input currency exist in the currency account. ie. to prevent invalid typing of currency like asdasd
# Check whether the input currency exist in the user's account
# Check whether the transfer currecy exist in the system, No then terminate , if yes check whether the user has this currency account
# If To_currency does not exist in the user account, create a new key in the balance dictionary
# If exitst, just edit the value within the dictionary
                
    FROM_currency=input("FROM_currency: \n")
    if FROM_currency not in currency:
        print("There is no this currency in the system")
        return False
    else:
        if FROM_currency not in account[login]['balance']:
            print("You do not have ",FROM_currency,"account in your balance")
            return False
            
    TO_currency=input("TO_Currency: \n")
    if TO_currency not in currency:
        print("There is no this currency in the system")
        return False
    # Since the exchange_amount is of the TO_currency, therefore we have to divide it with the currency rate in the dictionary.
    # The value is stored in the variable rate(FROM_currency)  
    # Check the existence of the currency and whether the user has enought money to exchange  
    exchange_amount=int(input("The amount: \n"))
    rate=exchange_amount/currency[FROM_currency][TO_currency]
    if FROM_currency in account[login]['balance']:
        if TO_currency not in account[login]['balance']:
            print("A new account for ", TO_currency,"is automaticaly created for you\n")
            if account[login]['balance'][FROM_currency]>=rate:                
                account[login]['balance'][FROM_currency]-=rate
                account[login]['balance'][TO_currency]=0
                account[login]['balance'][TO_currency]+=exchange_amount
                print("##################################################")
                print("## {} ##".format("".center(width)))
                print("## {} ##".format("Exchange Sucessfully".center(width)))
                print("## {} ##".format("".center(width)))
                print("## {} ##".format("1. Check Balance".ljust(width)))
                print("## {} ##".format("2. Exit".ljust(width)))
                print("##################################################")
                check=input("Enter the option: ")
                if check=='1':
                    check_balance(account,login)
                else:
                    return True
            else:
                print("You have no enough money for this action ")
                return False
        else:
            account[login]['balance'][FROM_currency]-=rate            
            account[login]['balance'][TO_currency]+=exchange_amount
            print("##################################################")
            print("## {} ##".format("".center(width)))
            print("## {} ##".format("Exchange Sucessfully".center(width)))
            print("## {} ##".format("".center(width)))
            print("## {} ##".format("1. Check Balance".ljust(width)))
            print("## {} ##".format("2. Exit".ljust(width)))
            print("##################################################")
            check=input("Enter the option: ")
            if check=='1':
                check_balance(account,login)
            else:
                return True
    else:
        print("YA")
        return False
    return False
    
   

# welcome page

print("##################################################")
print("## {} ##".format("".center(width)))
print("## {} ##".format("Welcome to PyBank".center(width)))
print("## {} ##".format("".center(width)))
print("##################################################")
      
# Task 1: login validation

while login_tried<3:
    login = input("Login Name: ")
    if login in account.keys():        
        password=getpass.getpass(prompt='Password: ', stream=None)
        if password == account[login]['password']:
            key=random.choice(captcha_list)
            ver=input("Enter the following captcha to verify you are human: "+ key + "\nYour answer: ")
            if ver==key:
                print("Login Success")
                login_tried=4
                exit
            else:
                print("Incorrect captcha\n Please login again")
                         
        else:
            print("Wrong password")
            logging.basicConfig(format='%(asctime)s %(message)s')
            logging.warning('is when this event was logged.')
            login_tried+=1
            login_tried_tempt+=1
            print("You have attempted to login for " , login_tried , "times ")        
    else:
        print("There is no data for this individual")          
            
else:
    if login_tried==3:
        endProgram= True
    else:
        endProgram =False

####### Task 1 end

while not endProgram:
    # menu page
    # I add the latest login attempt using a new vairable login_tried_tempt as i dont want to mess up the original login_tried
    # which is used for escaping the while loop when login<3
    menuoption = ""

    while not menuoption in ["1", "2", "3", "4","5"]: 
        sen="Latest Login Attempt: " + str(login_tried_tempt)
        print("##################################################")
        print("## {} ##".format(sen.rjust(width)))
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("Please select service".center(width)))
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("1. Cash Withdrawal ".ljust(width)))
        print("## {} ##".format("2. Transfer".ljust(width)))
        print("## {} ##".format("3. Account Balance".ljust(width)))
        print("## {} ##".format("4. Currency Exchange".ljust(width)))
        print("## {} ##".format("5. Exit".ljust(width)))
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("#"*width))
        menuoption = input("Enter the option: ")

    else:
        if menuoption == "1":            
            endProgram = cash_withdrawal(account, login)
            input("Press Enter to continue...")
            
        elif menuoption == "2":
            endProgram = transfer(account, login)
            input("Press Enter to continue...")
            
        elif menuoption == "3":
            endProgram = check_balance(account, login)
            input("Press Enter to continue...")
            
        elif menuoption == "4":
            endProgram = currency_exchange(account, login)
            input("Press Enter to continue...")
            
        elif menuoption == "5":
            endProgram = True

print("Bye!")
input("Press Enter to end the program...")
