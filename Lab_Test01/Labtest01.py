# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 13:49:47 2020

@author: blraj
Name   : Rajkumar B L
Reg.no : 2047120
Course : MCS173 - lAB-TEST-01
MSC.Cs - 1st Year
"""
#%%
def decToMayanInHex(num):
    base=20
    hex_string=""
    while num>0:
        digit = int(num%base)
        if digit<10:
            hex_string += str(digit)
        else:
            hex_string += chr(ord('A')+digit-10)  
        num //= base
    hex_string = hex_string[::-1]  
    return hex_string
#%%

#%%
HexMayanDict={ '0':'#', '1':'o', '2':'oo', '3':'ooo', '4':'oooo',
           '5':'-', '6':'o-', '7':'oo-', '8':'ooo-', '9':'oooo-',
           'A':'--', 'B':'o--', 'C':'oo--', 'D':'ooo--','E':'oooo--',
           'F':'---','G':'o---','H':'oo---','I':'ooo---','J':'oooo---'}

def hexToMayan(hstring):
    mayn_list=[]
    hstring=hstring.upper()
    if len(hstring)>=1:
       for ch in hstring:
           if ch in HexMayanDict:
              mayn_list.append(HexMayanDict.get(ch))
           else:
             mayn_list=[]
             print("Invalid String!")
             break   
    return mayn_list

#%%

class notintpostivie(UserWarning): 
	pass 

def decToMayan(num):
    try: 
        number=int(num)
        if number<=0:
            raise notintpostivie
    except ValueError:
        print("\tYou have not intered an integer :(") 
    except notintpostivie:
        print("\tThe number entered is not positive") 
    else:
        num_hex_str=decToMayanInHex(num)
        return hexToMayan(num_hex_str)
        
   
   