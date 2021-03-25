# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:28:16 2021

@author: Immortal
"""

def palindrome(senetence):
    for i in (",.'?/><}{{}}'"):
        sentence =sentence.replace(i,"")
        palindrome=[]
        word =sentence.split('')
        for word in words:
            word =word.lower()
            if word ==word[::-1]:
                palindrome.append(word)
            return palindrome
       
        
 #Checking Whether string is palindrome or not.      
def check_palindrome(string):
    length = len(string)
    first = 0
    last = length -1 
    status = 1
    while(first<last):
           if(string[first]==string[last]):
               first=first+1
               last=last-1
           else:
               status = 0
               break
    return int(status)  
string = input("Enter the string: ")
print("Method 1")
status= check_palindrome(string)
if(status):
    print("It is a palindrome ")
else:
    print("Sorry! Try again")