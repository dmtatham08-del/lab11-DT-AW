# https://github.com/dmtatham08-del/lab11-DT-AW/tree/main
# Partner 1: David Tatham
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

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0 or a==1:
        raise ValueError
    if b <=0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    try:
        math.sqrt(a)
    except ValueError:
        raise ValueError()
    else:
        return math.sqrt(a)

def hypotenuse(a,b):
    try:
        math.hypot(a,b)
    except Exception as e:
        raise e
    else:
        return math.hypot(a,b)