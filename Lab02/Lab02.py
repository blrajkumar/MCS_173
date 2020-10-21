# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:54:29 2020

@author: blraj
Name   : Rajkumar B L
Reg.no : 2047120
Course : MCS173 - lAB02
MSC.Cs - 1st Year

"""
#%%
user_info={"raj":"raj123", "hareesma" : "hareesma123" , "admin" : "admin123"}
pass_retr_ques={"raj":["Your mother's maiden name? ", "Kuppusamy"],
                "hareesma":["Your pet name? ", "hari"]}

def sign_in(username,password):
  attempt = 0
  login = False
  while(attempt<3 and (not login)):
    if username in user_info:
        user_pass = user_info.get(username)
        if user_pass == password:
            __logged_in(username, password)
            login = True
        else:
            attempt += 1
            print("Authentication Failure!")
            password = input("Enter Password again: ") 
            
    else:
        attempt += 1
        print("Authentication Failure!")
        username = input("Enter username again: ") 
        password = input("Enter password again: ") 
        
  if (attempt == 3):
        __pass_retr()
        
  #End-Note      
  print("\n=======================================")
  print("|          Have a nice day             |")
  print("=======================================")   

#Helper-Method 1   

def __logged_in(username, password):
    
    if username == "admin":
         print("Login Successfull - ",username) 
         print("=======================================")
         print("      Displaying all user details      ")
         print("=======================================")
         for user in user_info:
           if(not user == "admin"):
             print("Username:",user,"\tPassword:",user_info.get(user))
         print("=======================================")
    else:
        print("=======================================")
        print("      Login Successfull - ",username) 
        print("=======================================")
        choice = input("Would you like to change the password? y/N --> ")
        valid_choice = False
        while(not valid_choice):
            if choice == 'y' or choice == 'Y':
                valid_choice = True
                new_user_pass=input("Enter new password: ")
                user_info[username]=new_user_pass
                if user_info.get(username) == new_user_pass:
                  print("Password changed Succesfully!")
            elif choice == 'n' or choice == 'N':
                valid_choice = True
                print("Thank you",username)
            else:
                choice=input("Invalid choice! Try again with y/N --> ")
        
#Helper-Method 2         
def __pass_retr():
    print("\n=======================================")
    print("|          Password Retrieval          |")
    print("=======================================")
    username = input("Enter username: ")  
    if username in pass_retr_ques and username in user_info: 
        user_ans= input(pass_retr_ques.get(username)[0])
        crct_ans = pass_retr_ques.get(username)[1]
        if user_ans == crct_ans:
            print(username,"your password is:",user_info.get(username))
            __logged_in(username, crct_ans)
        else:
            print("Sorry, Bad Luck",username)
    else:
        print("Not vaid username. Better luck next time!")
            
#%%