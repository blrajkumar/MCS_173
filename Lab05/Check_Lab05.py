# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:54:21 2020

@author: blraj
Name   : Rajkumar B L
Reg.no : 2047120
Course : MCS173 - lAB05
MSC.Cs - 1st Year
"""
import bms

class demo:
    def main():
        auth="*"*40
        eqsym="="*73
        minsym="-"*18
        
        
        print("\n" + auth + "\n*\t\t\t\t\t\t\t\t\t   *")
        print("*\t\tName   : Rajkumar B L\t\t   *")
        print("*\t\tReg.no : 2047120\t\t\t   *")
        print("*\t\tCourse : MCS173 - lAB05\t\t   *")
        print("*\t\t\t\t\t\t\t\t\t   *\n"+auth+"\n")
        
        
        #Create array of objects for Book ie create multiple objects of Book for array of object         
        b1 = bms.Book('CS','Java','Prabhu',2016)
        b2 = bms.Book('Maths','Discrete Math','Sandeep',2019)
        b3 = bms.Book('CS','ADBMS','Nismon',2020)
        b4 = bms.Book('HED','Respect','Manjunath',2020)
        b5 = bms.Book('CS','Unix','Chandra',2013)
        
        bs = []
        bs.append(b1)
        bs.append(b2)
        bs.append(b3)
        bs.append(b4)
        bs.append(b5)
        
        #Create a single object of FacultyMember called facultymember.
        facultymember = bms.FacultyMember('120', 'Tulasi', 'Co-ordinator', 'Computer Science',bs)
        
        #Print the title of the last object in array of object (Book)
        print("Title of the last book borrowed is","\"",bs[len(bs)-1].Title,"\"")
        
        #Accept the index number and string
        indx = int(input("Enter the index: "))
        newTitle = input("Enter the new title: ") 
        
        #Call UpdateBooks() with index(int),title(String) variables which replaces the title of the
        #object at the given index with the variable being passed to the method and print the
        #title of the Book which got modified
        print("\nOld title of the book at index:",indx ,'was',facultymember.UpdateBooks(indx,newTitle))
        
        
        #Accept another string for title
        newObjTitle = input("Enter the new title: ") 
        
        #Call UpdateBooks() with variables index(int), replbook(Book) [use the index
        #earlier accepted] and print the title of earlier existing object.
        rplbook = bms.Book('CS',newObjTitle,'Rajkumar',2013)
        print("\nOld title of the book at index:",indx ,'was',facultymember.UpdateBooks(indx,rplbook),"\n")
        
        
        #For my understanding - Printing list of all borrowed books after executing above ins 
        print(eqsym+"\n\t\t\t\t\tList of books borrowed by",facultymember.Name,"\n"+eqsym+"\n")
        i=1
        for b in facultymember.books:
            print(i,".",b.getBookDetails(),"\n")
            i+=1
        print(eqsym)
    
    if __name__=="__main__":
        main()

