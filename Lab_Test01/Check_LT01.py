# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 15:03:49 2020

@author: blraj
@author: blraj
Name   : Rajkumar B L
Reg.no : 2047120
Course : MCS173 - lAB-TEST-01
MSC.Cs - 1st Year
"""

import Labtest01

auth="*"*40
eqsym="="*55
minsym="-"*18


print("\n" + auth + "\n*\t\t\t\t\t\t\t\t\t   *")
print("*\t\tName   : Rajkumar B L\t\t   *")
print("*\t\tReg.no : 2047120\t\t\t   *")
print("*\t\tCourse : MCS173 LAB-TEST-01    *")
print("*\t\t\t\t\t\t\t\t\t   *\n"+auth+"\n")

#%%

#Execution of Reverse Compliment DNA Function
 
print(eqsym+"\n\tConverting the decimal values to the Mayan \n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> decToMayan(173)")
print("\tResult -->",Labtest01.decToMayan(173))
print()

print("Case 02:\n\tFunc   --> decToMayan(815)")
print("\tResult -->",Labtest01.decToMayan(815))
print()

print("Case 03:\n\tFunc   --> decToMayan(4285)")
print("\tResult -->",Labtest01.decToMayan(4285))
print()

print("Case 04:\n\tFunc   --> decToMayan(2047120)")
print("\tResult -->",Labtest01.decToMayan(2047120))
print()

print("Case 05:\n\tFunc   --> decToMayan(-20)")
print("\tResult -->",Labtest01.decToMayan(-20))
print()

print("Case 06:\n\tFunc   --> decToMayan('two')")
print("\tResult -->",Labtest01.decToMayan('two'))
print("\n"+eqsym+"\n")

#%%

print("Hey! I would like to tell you your DOB in Mayan system!!!")
year = int(input("Please enter your the year you were born: ") )
date = int(input("Please enter your the date you were born: ") )
dob=year+date
print("\nWoah! Your DOB in Mayan system is -->",Labtest01.decToMayan(dob))



