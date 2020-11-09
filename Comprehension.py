# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FRuLtfTlvlZRQN83bucrAVSv4iDDihGe
"""

# Python's list comprehensions are awesome.

#vals = [expression 
#        for value in collection 
  #      if condition]

# This is equivalent to:

#vals = []
#for value in collection:
 #   if condition:
  #      vals.append(expression)

# Example:

even_squares = [x * x for x in range(10) if not x % 2]
even_squares