# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:15:05 2020

@author: blraj
"""

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    side1=float(input("Enter length of side one: "))
    side2=float(input("Enter length of side two: "))
    side3=float(input("Enter length of side three: "))
    s=0.5*(side1+side2+side3)
    root=s*(s-side1)*(s-side2)*(s-side3)
    sq_rt=root**0.5
    print("Area of a triangle with sides",side1,side2,side3,"is",sq_rt)