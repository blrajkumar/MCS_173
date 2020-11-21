# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:00:37 2020

@author: blraj
"""

import Lab04
auth="*"*40
eqsym="="*40
minsym="-"*13

print("\n" + auth + "\n*\t\t\t\t\t\t\t\t\t   *")
print("*\t\tName   : Rajkumar B L\t\t   *")
print("*\t\tReg.no : 2047120\t\t\t   *")
print("*\t\tCourse : MCS173 - lAB04\t\t   *")
print("*\t\t\t\t\t\t\t\t\t   *\n"+auth+"\n")


#%%

#Execution of Reverse Compliment DNA Function
 
print(eqsym+"\n\tRunning Function  - Stock Profit\n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> stockpft([1,2,1,7,3,4,5])")
print("\tResult --> ",Lab04.stockpft([1,2,1,7,3,4,5]))

print("Case 02:\n\tFunc   --> stockpft([1,2,1,7,9,3,4,5])")
print("\tResult --> ",Lab04.stockpft([1,2,1,7,9,3,4,5]))

print("Case 03:\n\tFunc   --> stockpft([1,2,3,4,5])")
print("\tResult --> ",Lab04.stockpft([1,2,3,4,5]))

print("Case 04:\n\tFunc   --> stockpft([9,1,7])")
print("\tResult --> ",Lab04.stockpft([9,1,7]))

print("\n"+minsym+"  END FUNC 01 "+minsym+"\n")


#%%


#%%

#Execution of Chicking if number is pronic Function
 
print("\n"+eqsym+"\n\t\tRunning Function  - Rob\n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> rob([])")
print("\tResult --> ",Lab04.rob([]))

print("Case 02:\n\tFunc   --> rob([9,5])")
print("\tResult --> ",Lab04.rob([9,5]))

print("Case 03:\n\tFunc   --> rob([1,2,3,4,5])")
print("\tResult --> ",Lab04.rob([1,2,3,4,5]))

print("Case 03:\n\tFunc   --> rob([5,1,1,9,7,2,3])")
print("\tResult --> ",Lab04.rob([5,1,1,9,7,2,3]))

print("\n"+minsym+"  END FUNC 02 "+minsym+"\n")


#%%