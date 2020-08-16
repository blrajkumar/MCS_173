# -*- coding: utf-8 -*-
"""
MCS 173(Python) - Lab01_question01
Student Name: Rajkumar B L
Reg.NO      : 2047120
Email       : rajkumar.bl@cs.christumiversity.in



Question:1.	Given two integers C and U, return any string S such that:
S has length C + U and contains exactly C 'c' letters, and exactly U 'u' letters;
The substring 'ccc' does not occur in S;
The substring 'uuu' does not occur in S.
 
Example 1:
Input: C = 1, U = 2
Output: "cuu"
Explanation: "cuu", "ucu" and "uuc" are all correct answers.
Example 2:
Input: C = 4, U = 1
"""
def find_sub_string(c,u):
    sub_string= ""
    
    while (0 < c or 0 < u):
        if(c < u):
            if(0 < u):
                sub_string = sub_string+'u'
                u -=1
            if(0 < u):
                sub_string = sub_string+'u'
                u -=1
            if(0 < c):
                sub_string = sub_string+'c'
                c -=1
        elif (u < c):
            if(0 < c):
                sub_string = sub_string+'c'
                c -=1
            if(0 < c):
                sub_string = sub_string+'c'
                c -=1
            if (0 < u):
                sub_string = sub_string+'u'
                u -=1
        else:
            if(0 < c):
                sub_string = sub_string+'c'
                c -= 1
            if(0 < u):
                sub_string = sub_string+'u'
                u -=1
    print("\nOne possible substring is: ",sub_string)
 
   
c=int(input("Enter the integer value for C in range 1 - 100: "))
while(c not in range(1,101)):
    print("\nInput c out of range! Try again.")
    c=int(input("Enter the integer value for C in range 1 - 100: "))
    
u=int(input("Enter the integer value for U in range 1 - 100: "))
while(u not in range(1,101)):
    print("\nInput u out of range! Try again.")
    u=int(input("Enter the integer value for U in range 1 - 100: "))

if(u < c):
    if(c <= ((u * 2) + 2) ):
        find_sub_string(c,u)
    else:
        print("\nSubstring cannot be formed from the input values of C and U")
elif(c < u):
     if(u <= ((c * 2) + 2) ):
        find_sub_string(c,u) 
     else:
        print("\nSubstring cannot be formed from the input values of C and U")
else:
    find_sub_string(c,u) 
    