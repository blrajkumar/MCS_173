# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:13:53 2020

@author: blraj
"""

import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    alist=[]
    while len(alist)<10:
        item=random.random()
        item=(item*5)+30
        alist.append(item)
    print(alist)