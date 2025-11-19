#https://github.com/dmtatham08-del/lab11-DT-AW, David was p1, Ashley was p2
import math
def add(a, b): 
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a==0:
        raise ZeroDivisionError()
    else:
        return b/a
def log(a,b):
    if a==1 or a<=0:
        raise ValueError()
    elif b<=0:
        raise ValueError()
    else:
        return math.log(b, a)
def exp(a,b):
    return a**b
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
