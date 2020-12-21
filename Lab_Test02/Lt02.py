# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:03:57 2020

@author: blraj
"""

import pandas as pd
import matplotlib.pyplot as pt

auth="*"*40
eqsym="="*47
minsym="-"*18


print("\n" + auth + "\n*\t\t\t\t\t\t\t\t\t   *")
print("*\t\tName   : Rajkumar B L\t\t   *")
print("*\t\tReg.no : 2047120\t\t\t   *")
print("*\t\tCourse : MCS173 LAB-TEST-02    *")
print("*\t\t\t\t\t\t\t\t\t   *\n"+auth+"\n")

#%%
print(eqsym+"\n\t\t\t\tQuestion 01 \n"+eqsym)
print("Printing the top three powerfull cars:")
df = pd.read_csv('Automobile_data.csv')
top3 = df.loc[(df['wheel-base'] > 90) & (df['horsepower'] > 150) | (df['length'] > 190)]
top3 = top3.sort_values(['horsepower', 'price'], ascending=[0,1]).head(3)
print(top3['company'].to_string())
print(eqsym+"\n\n\n")
#%%

#%%
print(eqsym+"\n\t\t\t\tQuestion 02 \n"+eqsym)
print("Printing Sedan type cars manufactured in Germany:")
df2 = pd.read_csv('Automobile_data.csv')
germ = df.loc[((df['company'] == 'mercedes-benz') | (df['company'] == 'audi') | (df['company'] == 'bmw') | (df['company'] == 'porsche') | (df['company'] == 'volkswagen')) & (df['body-style'] == 'sedan') ]
print(germ)
print(eqsym+"\n\n\n")
#%%

#%%
print(eqsym+"\n\t\t\t\tQuestion 03 \n"+eqsym)
print("Printing wish list with cars having max price: ")
df3 = pd.read_csv('Automobile_data.csv')
highprice = df3.groupby('company').agg({'price': ['max']}) 
highprice = highprice.reset_index()
highprice.columns = ['Company','Max-Price']
#highprice.sort_values(by=['Max-Price'], inplace=True, ascending=True)
print(highprice)
print(eqsym+"\n\n\n")
#%%

#%%
print(eqsym+"\n\t\t\t\tQuestion 04 \n"+eqsym)
print("Plotting Line graph for the companys profit:")
df4 = pd.read_csv('company_sales_data.csv')
pic = pt.figure(figsize = (11, 7)) 
pt.title("Line Chart representing company's profit along the months") 
x = df4['month_number']
y = df4['total_profit']
pt.plot(x, y)
pt.xticks(df4.index+1, df4['month_number'], rotation=0)
pt.xlabel("Month") 
pt.ylabel("Profit") 
pt.show()
print(eqsym+"\n\n\n")
#%%

#%%
print(eqsym+"\n\t\t\t\tQuestion 05 \n"+eqsym)
print("Plotting bar graph for the companys profit:")
df5 = pd.read_csv('company_sales_data.csv')
pic = pt.figure(figsize = (11, 7))  
pt.title("Bar chart representing company's profit along the months")
x = df5['month_number']
y = df5['total_profit']
pt.bar(x, y, color ='Red', width = 0.4)
pt.xlabel("Month") 
pt.ylabel("Profit") 
pt.xticks(df4.index+1, df4['month_number'], rotation=0)
pt.show()

highprice = df5.sort_values(['total_profit']).tail(1)
print("The month with highest profit and its details is: ")
print(highprice.to_string())
print(eqsym+"\n\n\n")

#%%