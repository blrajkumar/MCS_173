# -*- coding: utf-8 -*-
"""
MCS 173(Python) - Lab01_question02
Student Name: Rajkumar B L
Reg.NO      : 2047120
Email       : rajkumar.bl@cs.christumiversity.in



Question:2.	Given a list, rotate the list to the right by k places, where k is non-negative.
Example 1:
Input: [1,2,3,4,5] k = 2
Output: [4,5,1,2,3]
Explanation:
rotate 1 steps to the right: [5,1,2,3,4]
rotate 2 steps to the right: [4,5,1,2,3]
"""
my_list=[1,2,3,4,5]
print("The Given list is:",my_list)
k=int(input("Enter the Number k for which the list is to be rotated: "))

while(k <= 0):
    print("\nPlease enter a positive k value.")
    k=int(input("Enter the Number k for which the list is to be rotated: "))
 
while(k not in range(1,len(my_list)+1)):
    print(k)
    k=k-len(my_list)
    
rot_list=(my_list[-k:] + my_list[:-k])
print("\nThe order of elements after k rotations in the list is:")
print(rot_list)
