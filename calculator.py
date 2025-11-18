# https://github.com/dmtatham08-del/lab11-DT-AW/tree/main
# Partner 1:
# Partner 2: Ashley Weiss

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return a / b

def log(a, b):
    if a == 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b
