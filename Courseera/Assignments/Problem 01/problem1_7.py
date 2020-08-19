# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:21:46 2020

@author: blraj
"""
def problem1_7():
   b1=float(input("Enter the length of one of the bases: "))
   b2=float(input("Enter the length of the other base: "))
   h=float(input("Enter the height: "))
   area=((b1+b2)/2)*h
   print("The area of a trapezoid with bases",b1,"and",b2,end=" ")
   print("and height",h,"is",area)
