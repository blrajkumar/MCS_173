# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:43:06 2020

@author: blraj
Name   : Rajkumar B L
Reg.no : 2047120
Course : MCS173 - lAB01
MSC.Cs - 1st Year

"""
#%%

land01 = ['c','c','c','c','c']

land02 = ['c','c','c','w','w']

land03 = ['c','c','c']

land04 = ['c','c','c','c','c','c','c','c','c','c']

land05 = ['c','c','c','c','c','w','w''w','w']

land06 = ['c','c','c','c','c','c','c','c','c','c']

land07 = ['w','w']

land08 = ['w','w','w','w','w','w']

Field =[]

Field.append(land04)
Field.append(land06)
Field.append(land07)

def watered_crop(field_list):
    watered=False
    w_count=0
    c_count=0
    for list in field_list:
        for resource in list:
            if resource == 'c':
                c_count+=1
            elif resource == 'w':
                w_count+=1
            else:
                pass
    if len(field_list) == 0:
     print("Invalid input")
     watered=False
    elif c_count == 0:
     watered=False 
    elif ((w_count*10)-c_count)>=0:
     watered=True 
    else:
     pass  
    return watered
#%%