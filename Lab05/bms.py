# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:31:25 2020

@author: blraj
Name   : Rajkumar B L
Reg.no : 2047120
Course : MCS173 - lAB05
MSC.Cs - 1st Year
"""

class Book:
    def __init__(self,Subject,Title,Publisher,Year_of_publication):
        self.Subject = Subject
        self.Title = Title
        self.Publisher = Publisher
        self.Year_of_publication = Year_of_publication
        
    def getBookTitle(self):
        return self.Title
    
    def getBookDetails(self):
        return 'Subject:'+self.Subject + ' || Title:'+self.Title + ' || Publisher:'+self.Publisher + ' || Year:'+str(self.Year_of_publication)
 
class FacultyMember:
    #books=None - means it can be called with or without this parameter 
    def __init__(self,Id,Name,Designation,Department,books=None):
        self.Id = Id
        self.Name = Name
        self.Designation = Designation
        self.Department = Department
        if books is None:
            self.books=[]
        else:
            self.books = books
    
    def UpdateBooks(self,index,repl):
        
        oldTitle = self.books[index].Title
        if(type(repl)==str):
           self.books[index].Title = repl
        elif(type(repl)==Book):
            self.books[index]= repl
        return oldTitle
   
