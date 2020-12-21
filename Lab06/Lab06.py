# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:24:34 2020

@author: blraj
Name   : Rajkumar B L
Reg.no : 2047120
Course : MCS173 - lAB06
MSC.Cs - 1st Year
"""
import re

class Lab06:
    def __init__(self):
         pass

    def time_tracker(self,curtime):
        time_result=""
        stopcode = re.compile(r'^([0]?[0-4]|2[2-3])(:[0-5][0-9])?$')
        keepcode = re.compile(r'^(0?[5-9]|1[0-9]|2[01])(:[0-5][0-9])?$')
        if stopcode.match(curtime):
            time_result = "Time to rest. Stop Coding Raj!!!"
        elif keepcode.match(curtime):
            time_result = "Great work raj. Keep coding!!!"
        else:
            time_result = "Invalid time format :("
        return time_result
                
    def is_decimal(self,val):
        dec_result=""
        decpattern = re.compile(r'^[0-9]+\.[0-9]+$')
        if decpattern.match(val):
            dec_result = "The input is decimal."
        else:
            dec_result = "Invalid format or is not decimal"
        return dec_result
            
    def acr_creator(self,inp_string):
        acr=""
        acr_result=""
        acr_pattern = re.compile(r'\b[a-zA-Z]')
        matches=acr_pattern.finditer(inp_string)
        for match in matches:
            acr+=match.group(0)
        if acr_pattern.match(inp_string):
            acr_result = "The acronym for given string is "+acr
        else:
            acr_result = "Invalid Input String !!!"
        return acr_result
    
    def rep_wordletrs(self,inp_string):
        rep_result = ""
        rep_pattern = re.compile(r'\b(\w+)\1\b')
        list_words=[]
        matches=rep_pattern.finditer(inp_string)
        for match in matches:
            list_words.append(match.group(0))    
        if list_words:
            rep_result = "The list of words with matching letters are "+str(list_words)         
        else:
            rep_result = "No matches !!!"
        return rep_result
            
auth="*"*40
eqsym="="*50
minsym="-"*18

lobj = Lab06()
       
print("\n" + auth + "\n*\t\t\t\t\t\t\t\t\t   *")
print("*\t\tName   : Rajkumar B L\t\t   *")
print("*\t\tReg.no : 2047120\t\t\t   *")
print("*\t\tCourse : MCS173 - lAB06\t\t   *")
print("*\t\t\t\t\t\t\t\t\t   *\n"+auth+"\n")

#Execution of Time Tracker Function
#%%
print(eqsym+"\n\tRunning Function  - Time Tracker\n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> time_tracker(\"12\")")
print("\tResult -->",lobj.time_tracker("12"))

print("Case 02:\n\tFunc   --> time_tracker(\"22:00\")")
print("\tResult -->",lobj.time_tracker("22:00"))

print("Case 01:\n\tFunc   --> time_tracker(\"5:01\")")
print("\tResult -->",lobj.time_tracker("5:01")) 

print("Case 01:\n\tFunc   --> time_tracker(\"two 'o' clock\")")
print("\tResult -->",lobj.time_tracker("two 'o' clock"))  
           
print("\n"+minsym+"  END FUNC 01 "+minsym+"\n")
#%%

#Execution of Is Decimal Function
#%%
print(eqsym+"\n\tRunning Function  - Is Decimal\n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> is_decimal(\"12345\")")
print("\tResult -->",lobj.is_decimal("12345"))

print("Case 02:\n\tFunc   --> is_decimal(\"123.456\")")
print("\tResult -->",lobj.is_decimal("123.456"))

print("Case 03:\n\tFunc   --> is_decimal(\"5199999999.99999999\")")
print("\tResult -->",lobj.is_decimal("5199999999.99999999"))

print("Case 04:\n\tFunc   --> is_decimal(\"5point34\")")
print("\tResult -->",lobj.is_decimal("5point34"))

            
print("\n"+minsym+"  END FUNC 01 "+minsym+"\n")

#%%
    
#Execution of Acronym Creator Function
#%%
print(eqsym+"\n\tRunning Function  - Acronym Creator\n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> acr_creator(\"National Aeronautics Space Administration\")")
print("\tResult -->",lobj.acr_creator("National Aeronautics Space Administration"))

print("Case 02:\n\tFunc   --> acr_creator(\"You Only Live Once\")")
print("\tResult -->",lobj.acr_creator("You Only Live Once"))

print("Case 03:\n\tFunc   --> acr_creator(\"Laugh Out Loud\")")
print("\tResult -->",lobj.acr_creator("Laugh Out Loud"))

print("Case 04:\n\tFunc   --> acr_creator(\"123 564\")")
print("\tResult -->",lobj.acr_creator("123 564"))
            
print("\n"+minsym+"  END FUNC 01 "+minsym+"\n")

#%%


#Execution of Finding Word Repeater Function
#%%
print(eqsym+"\n\tRunning Function  - Finding Word Repeater\n"+eqsym+"\n")

print("Case 01:\n\tFunc   --> rep_wordletrs(\"Hey murmur , how is tartar ?\")")
print("\tResult -->",lobj.rep_wordletrs("Hey murmur, how is tartar ?"))

print("Case 02:\n\tFunc   --> rep_wordletrs(\"Hello world\")")
print("\tResult -->",lobj.rep_wordletrs("Hello worldr"))

print("Case 03:\n\tFunc   --> rep_wordletrs(\"YAY! mama is making yumyum cake\")")
print("\tResult -->",lobj.rep_wordletrs("YAY! mama is making yumyum cake"))

            
print("\n"+minsym+"  END FUNC 01 "+minsym+"\n")

#%%