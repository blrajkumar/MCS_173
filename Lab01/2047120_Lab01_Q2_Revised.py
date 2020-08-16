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

rot_list=my_list 

print("Input: ",my_list)
print("Explanation:")
for i in range(0,k):
    rot_list=(rot_list[-1:] + rot_list[:-1])
    print("Rotate",i+1,"steps t0 the right: ",rot_list)
print("Output: ",rot_list)

    
"""
Effecient way of doing the above 
while(k not in range(1,len(my_list)+1)):
    k=k-len(my_list)
rot_list=my_list    
rot_list=(my_list[-k:] + my_list[:-k])

print("Doing",user_k,"rotations is similar to doing",k,"rotaions.")
print("Hency we only do",k,"rotations for effeciency.")
print("The order of elements after k rotations in the list is:") 
print(rot_list) 
"""
    