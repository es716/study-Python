#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#==============================================
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x
    
def power(x,n = 2):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if not isinstance(n,int):
        raise TypeError("bad operand type")
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):
    res = 0
    for n in numbers:
        res = res + n
    return res

def person(name, age, **kw):
    print('name:',name,'age:',age,'other:',kw)

def person1(name, age, *args, city, job):
    print(name, age, args, city, job)

def person2(name, age, *, city, job):
    print(name, age, city, job)
