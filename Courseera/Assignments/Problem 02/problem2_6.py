# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:14:35 2020

@author: blraj
"""

import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    alist=[]
    blist=[]
    while len(alist)<100 and len(blist)<100:
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        alist.append(dice1)
        blist.append(dice2)
        print(dice1+dice2)
        

