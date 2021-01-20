# -*- coding: utf-8 -*-
"""faulthandler.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PZbtRxluNmwfZKhHq3H-LLQwKvYaQ2HX
"""

# Python 3.3+ has a std
# lib module for displaying
# tracebacks even when Python
# "dies", e.g with a segfault:

import faulthandler
faulthandler.enable()

# Can also be enabled with
# "python -X faulthandler"
# from the command line.

# Learn more here:
# https://docs.python.org/3/library/faulthandler.html