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
        if(index<1 or index>5):
            oldTitle ='Invalid Index!'
        else:
            oldTitle = self.books[index-1].Title
            if(type(repl)==str):
               self.books[index-1].Title = repl
            elif(type(repl)==Book):
                self.books[index-1]= repl
        return oldTitle
   
def main():
    auth="*"*40
    eqsym="="*73
  
    print("\n" + auth + "\n*\t\t\t\t\t\t\t\t\t   *")
    print("*\t\tName   : Rajkumar B L\t\t   *")
    print("*\t\tReg.no : 2047120\t\t\t   *")
    print("*\t\tCourse : MCS173 - lAB05\t\t   *")
    print("*\t\t\t\t\t\t\t\t\t   *\n"+auth+"\n")
    
    #Create array of objects for Book ie create multiple objects of Book for array of object         
    b1 = Book('CS','Java','Prabhu',2016)
    b2 = Book('Maths','Discrete Math','Sandeep',2019)
    b3 = Book('CS','ADBMS','Nismon',2020)
    b4 = Book('HED','Respect','Manjunath',2020)
    b5 = Book('CS','Unix','Chandra',2013)
    
    bs = []
    bs.append(b1)
    bs.append(b2)
    bs.append(b3)
    bs.append(b4)
    bs.append(b5)
    
    #Create a single object of FacultyMember called facultymember.
    facultymember = FacultyMember('120', 'Tulasi', 'Co-ordinator', 'Computer Science',bs)
    
    #For my understanding - Printing list of all borrowed books after executing above ins 
    print(eqsym+"\n\t\t\t\t\tList of books borrowed by",facultymember.Name,"\n"+eqsym+"\n")
    i=1
    for b in facultymember.books:
        print(i,".",b.getBookDetails(),"\n")
        i+=1
    print(eqsym)
    
    
    #Print the title of the last object in array of object (Book)
    print("\nTitle of the last book borrowed is","\"",bs[len(bs)-1].Title,"\"")
    
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
    rplbook = Book('CS',newObjTitle,'Rajkumar',2013)
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
