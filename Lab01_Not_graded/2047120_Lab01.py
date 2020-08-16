# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:23:26 2020
@author: blraj

Name   : Rajkumar B L
Reg.no : 2047120
Course : MCS173 - lAB01
MSC.Cs - 1st Year

"""


#%%
"""
Question - 01
Write a function for checking the speed of drivers.
"""

def driver(speed):
    dest="n"
    demerit=0
    while speed%5 != 0:
        speed = int(input("Invalid speed. Enter agian: "))
    if speed % 5 == 0:
        while dest =="N" or dest=="n":
            if speed<=70:
                print("You are doing fine! maintain this speed and stay safe :)")
            elif speed>70:
                demerit=demerit+((speed-70)/5)
                print("You are driving over the speed limit of 70km/hr.", end="\n")
                print("You are given with",(speed-70)/5,"demerit point(s).",end="\n")
                print("Your total demrit points: ",demerit)
                if demerit>=12:
                    print("Your license is suspended for 6 months.",end="\n")
                    print("Please contact Mrs.Tulasi.")
                    dest="y"
                    break
                else:
                    print("Please follow the speed limit.")
            else:
                pass
            dest=input("Have you reached your destination y|n: ")
            while dest.lower() != "y" and dest.lower() != "n":
                dest=input("Invalid entry. Enter y|n: ")

            if dest=="N" or dest=="n":
                speed=int(input("Enter your current Speed: "))
                while speed.isnotdigit():
                    while speed%5 !=0:
                        speed=int(input("Invalid speed. Enter agian: "))
                
            elif dest=="Y" or dest=="y":
                print("Have a nice day!")
            else:
                print()
                

#%%


#%%
"""
Question - 02
Write a function which takes in a string and prints if it is a pangram or not.
"""
alpa = []
def pangram(strng):
    strng = strng.lower()
    for ch in strng:
        if ch not in alpa and ch != " " :
         alpa.append(ch)
    if len(alpa)==26:
        print("YAAY! The given string is a pangram")
        del alpa[0:len(alpa)]
    
    elif len(alpa)>0 and len(alpa)<26:
        print("OOPS! The given string is not a pangram")
        del alpa[0:len(alpa)]
     
    elif len(alpa)==0:
        print(" :{ Please enter a valid string to check the pangram property")
        del alpa[0:len(alpa)]
 
    else:
        pass
        
    
#%%


#%%
"""
Question - 03
Write a function  select the captain of the worst team ( List of lists).
"""

Team01 = ["FAAIZ","GAURAV","KARTHIK","SIVA","CHANCHAL","PARIDHI","GANDHI","AAYUSH"]

Team02 = ["ABHAY","ABHINAV","LAXMY","MANSOOR","MANSI","NIYA","SHRAAVYA","ANGEL"]

Team03 = ["SHREYANSH","ADITYA","KSHITIZ","RUDRESH","DEEKSHA","CHUI","NAMRATHA","VAISHNAVI"]

Team04 = ["APOORVA","SAMEER","SHIVAM","AISHWARYA","NAYANIKA","NEERAJA","TIYASHA"]

Team05 = ["ADARSH","ARCHISMAN","BISHAL","HARI","SHRINI","SWARNAVA","NISCHITHA","HARISH","MOHAK","MOHIT"]

Team06 = ["ADWAITH","DEVARAJ","RAJKUMAR","TEJAS","ANJALI","SONALI","YASHASHWINI"]

Team07 = ["ADARSH TAKUR","DEV","DHIRENDRA","KANISHKA","SUMIT","VIVEK","AKANKSHA","PITCHAYUT","MAYANK"]

MCSL = []
MCSL.append(Team01)
MCSL.append(Team02)
MCSL.append(Team03)
MCSL.append(Team04)
MCSL.append(Team05)
MCSL.append(Team06)
MCSL.append(Team07)

def team_cap(alist):   
    team_count = 0
    while team_count < len(alist):
        print("====================",end="\n")
        if team_count==0:
            print("Team:",team_count+1,"(Best Team)",end="\n")
        elif team_count==(len(alist)-1):
            print("Team:",team_count+1,"(Worst Team)",end="\n")
        else:
            print("Team:",team_count+1,end="\n")
        print("Coach:",alist[team_count][team_count],"\nCaptain:",alist[team_count][team_count+1],end="\n")
        team_count=team_count+1
     

#%%

