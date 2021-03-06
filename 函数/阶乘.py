#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756044276a15558a759ec43de8e30eb0ed169fb11000
#http://www.cnblogs.com/joinclear/archive/2013/02/06/2908247.html

#递归函数--阶乘 问题

num = input("输入阶乘数：")

#递归
def recursive(n):
    if n == 1:
        return 1
    else:
        return recursive(n-1)*n
    
#尾递归
def jiecheng(n):
    return jc(n,1)

def jc(n,res = 1):
    if n == 1:
        return res*n
    else:
        return jc(n-1,res*n)

print("尾递归函数--阶乘")
print(recursive(int(num)))

print("递归函数--阶乘")
print(jiecheng(int(num)))
