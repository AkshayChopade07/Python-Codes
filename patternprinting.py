# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 23:05:59 2020

@author: Immortal
"""

#Printing Pattern
rows =10
for i  in range(1,rows+1):
    #print("\n")
  
    print("*" * i)
    
    
    


#Identifying URL's IP Address
import socket as s
url='www.facebook.com'
print(f'IP of {url} is {s.gethostbyname(url)}')   