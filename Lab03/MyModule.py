# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 21:15:58 2020

@author: blraj
Name   : Rajkumar B L
Reg.no : 2047120
Course : MCS173 - lAB03
MSC.Cs - 1st Year
"""
#%%
def reversecompliment_DNA(dnaStr):
   revdnastr=""
   revCompDNA={"A":"T", "C":"G" , "T":"A", "G":"C"}
   
   if len(dnaStr)>=1:
       for ch in dnaStr[ : : -1]:
           if ch in revCompDNA:
             revdnastr += revCompDNA.get(ch)
           else:
             revdnastr="Not Valid DNA String!"
             break
   else:
       revdnastr="Not Valid DNA String!"

   return revdnastr
#%%


#%%
def check_if_pronic(pronint):
   ckStr=str(pronint)+" is Not Pronic!" 
   for i in range(1,pronint+1):
       if ( (i*(i+1)) == pronint ):
           ckStr=str(pronint) + " is pronic for Consecutive Integers(" + str(i) + "," + str(i+1) + ")"
           break
   return ckStr
#%%

#%%
morseEnCodeDict={ 'A':'.- ', 'B':'-... ', 
               'C':'-.-. ', 'D':'-.. ', 'E':'. ', 
               'F':'..-. ', 'G':'--. ', 'H':'.... ', 
               'I':'.. ', 'J':'.--- ', 'K':'-.- ', 
               'L':'.-.. ', 'M':'-- ', 'N':'-. ', 
               'O':'--- ', 'P':'.--. ', 'Q':'--.- ', 
               'R':'.-. ', 'S':'... ', 'T':'- ', 
               'U':'..- ', 'V':'...- ', 'W':'.-- ', 
               'X':'-..- ', 'Y':'-.-- ', 'Z':'--.. ', 
               '1':'.---- ', '2':'..--- ', '3':'...-- ', 
               '4':'....- ', '5':'..... ', '6':'-.... ', 
               '7':'--... ', '8':'---.. ', '9':'----. ', 
               '0':'----- ', ', ':'--..-- ', '.':'.-.-.- ', 
               '-':'-....- ', '@':'.--.-', ' ':'/'} 

morseDeCodeDict = {}
for k, v in morseEnCodeDict.items():
    morseDeCodeDict[v] = k

def encode(mstring):
    code=""
    mstring=mstring.upper()
    if len(mstring)>=1:
       for ch in mstring:
           if ch in morseEnCodeDict:
             code += morseEnCodeDict.get(ch)
           else:
             code="Not Valid Input String!"
             break
    else:
       code="Not Valid Input String!"

    return code

def decode(mstring):
    code=""
    if len(mstring)>=1:
       for wrd in mstring.split(' /'):
           for ch in wrd.split():
               if (ch+" ") in morseDeCodeDict:
                 code += morseDeCodeDict.get(ch+" ")
               else:
                 code="Not Valid Input String!"
                 break
           code += " "
    else:
       code="Not Valid Input String!"
    return code
    

#%%

