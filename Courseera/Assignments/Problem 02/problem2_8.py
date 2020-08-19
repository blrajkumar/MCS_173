# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:15:26 2020

@author: blraj
"""

hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]
def problem2_8(temp_list):
    ahl=[0.0,temp_list[0],temp_list[0]]
    for i in temp_list:
        ahl[0]=ahl[0]+i
        if ahl[1]<i:
            ahl[1]=i  
        elif ahl[2]>i:
            ahl[2]=i
        else:
            pass
    ahl[0] = ahl[0]/len(temp_list)
    print("Average:",ahl[0])
    print("High:",ahl[1])
    print("Low:",ahl[2])