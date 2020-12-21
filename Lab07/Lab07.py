# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 00:49:40 2020

@author: blraj
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as pt

auth="*"*40
eqsym="="*40
minsym="-"*13

print("\n" + auth + "\n*\t\t\t\t\t\t\t\t\t   *")
print("*\t\tName   : Rajkumar B L\t\t   *")
print("*\t\tReg.no : 2047120\t\t\t   *")
print("*\t\tCourse : MCS173 - lAB07\t\t   *")
print("*\t\t\t\t\t\t\t\t\t   *\n"+auth+"\n")


df = pd.read_csv('supermarket_sales.csv')

#%%
print(eqsym+"\n\t\t\t\tQuestion 01 \n"+eqsym)
print("Top three products sold:")
valcnt= df['Product line'].value_counts(dropna=True).head(3)
tops1 = pd.DataFrame(valcnt)
topsales = tops1.reset_index()
topsales.columns = ['Product_Line','Count']
topsales.sort_values(by=['Count'], inplace=True, ascending=False)
print(topsales)
pic = pt.figure(figsize = (15, 7))
pt.rcParams['font.size'] = 16
pt.title('Top three products sold')
pt.pie(topsales.Count, labels = topsales.Product_Line,autopct='%.2f %%',textprops={'color':"black",'fontsize': 18},colors=['#003f5c','g','b']) 
pt.show() 
print(eqsym+"\n\n\n")
#%%


#%%
print(eqsym+"\n\t\t\t\tQuestion 02 \n"+eqsym)
print("Who shops more male/female?")
gndr=df['Gender'].value_counts()
gndr = gndr.reset_index()
gndr.columns = ['Gender','Count']
pic = pt.figure(figsize = (15, 11))
pt.title('Pie chart to show the purchase %')
pt.pie(gndr.Count, labels = gndr.Gender,autopct='%.2f %%',colors=['#003f5c','g']) 
pt.show() 
print("\nTherefore the gender that shops more is:")
print(gndr.head(1))
print(eqsym+"\n\n\n")
#%%


#%%
def plotting_overallsale(ylabtit,titstr,lst):
    barWidth = 0.25
    allbranchsale = lst
    
    a=allbranchsale['A']
    ta = a.reset_index()
    ta.columns = ['Product_Line','Count'] 
    
    b=allbranchsale['B']
    tb = b.reset_index()
    tb.columns = ['Product_Line','Count'] 
    
    c=allbranchsale['C']
    tc = c.reset_index()
    tc.columns = ['Product_Line','Count']
    
    # set height of bar
    bars1 = ta.Count
    bars2 = tb.Count
    bars3 = tc.Count
     
    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
     
    # Make the plot
    pic = pt.figure(figsize = (15, 9))
    pt.rcParams['font.size'] = 11
    title="Bar chart representing product sale "+titstr+" across different branches"
    pt.title(title,fontweight='bold')
    pt.bar(r1, bars1, color='#003f5c', width=barWidth, edgecolor='white', label='Branch - A')
    pt.bar(r2, bars2, color='g', width=barWidth, edgecolor='white', label='Branch - B')
    pt.bar(r3, bars3, color='b', width=barWidth, edgecolor='white', label='Branch - C')
     
    # Add xticks on the middle of the group bars
    pt.xlabel('Product_Line', fontweight='bold')
    pt.ylabel(ylabtit, fontweight='bold')
    pt.xticks([r + barWidth for r in range(len(bars1))],ta.Product_Line)
     
    # Create legend & Show graphic
    pt.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
    pt.show()
#%%

#%%
print(eqsym+"\n\t\t\t\tQuestion 03 \n"+eqsym)
print("\nPlotting the sales count as per branch:")
allbranchsale = df.groupby(['Branch','Product line'])["Quantity"].sum()
plotting_overallsale("Qunatity","quantity",allbranchsale)
    
print("\n\n\nPlotting the sales - gross income as per branch:")
allbranchsale = df.groupby(['Branch','Product line'])["gross income"].sum()
plotting_overallsale("Gross_Income","gross income",allbranchsale)
print("\n"+eqsym+"\n\n\n")
 #%%   

