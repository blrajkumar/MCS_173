# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:59:59 2020

@author: blraj
Name   : Rajkumar B L
Reg.no : 2047120
Course : MCS173 - lAB04
MSC.Cs - 1st Year
"""

stockpft=lambda stock: max([[stock[i] - stock[j]] for i in range(len(stock)-1,0,-1) for j in range(i-1,-1,-1)])

rob = lambda house : 0 if len(house)==0 else(house[0] if len(house)==1 else (max(house) if len(house)==2 else(rob3(house))))

def rob3(house):
    rbval=[0]*len(house)
    rbval[0] = house[0]
    rbval[1] = max(house[0], house[1])
    for i in range(2, len(house)):
        rbval[i] = max(rbval[i-1],rbval[i-2]+house[i])
    amount = rbval[len(rbval)-1]
    return int(amount)
