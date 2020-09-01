# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:24:06 2020

@author: Immortal
"""


test_list =[9,3,12,8,2,1,7]
test_list1 =[7,11,12,1,98,2]
#printing original lists
print("The original list 1 is:"+str(test_list))
print("The Original list 2 is:"+str(test_list1))


#percentage Similarity of lists
#using "|"operator + "&" operator +set()

res=len(set(test_list)&set(test_list1))/float(len(set(test_list)|set(test_list1)))*100

#printing results
print("Percentage similarity among lists is:"+str(res))






#By taking user input


test_list =input("Enter 7 values of list1 :")
test_list1 =input("Enter 7 values of list12 :")
#printing original lists
print("The original list 1 is:"+str(test_list))
print("The Original list 2 is:"+str(test_list1))


#percentage Similarity of lists
#using "|"operator + "&" operator +set()

res=len(set(test_list)&set(test_list1))/float(len(set(test_list)|set(test_list1)))*100

#printing results
print("Percentage similarity among lists is:"+str(res))