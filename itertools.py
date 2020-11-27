# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:27:13 2020

@author: Immortal
"""

# itertools.permutations() generates permutations 
# for an iterable. Time to brute-force those passwords ;-)

import itertools
for p in itertools.permutations('ABCD'):
    print (p)
