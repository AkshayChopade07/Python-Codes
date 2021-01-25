# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 23:19:07 2021

@author: Immortal
"""
#The open() function returns a file object
f = open("demofile.txt", "r")
print(f.read())



#Open a file on a different location:

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

#Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))

#Read one line of the file:

f = open("demofile.txt", "r")
print(f.readline())

#Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

#Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x)
  
#Close the file when you are finish with it:

f = open("demofile.txt", "r")
print(f.readline())
f.close()

