#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756044276a15558a759ec43de8e30eb0ed169fb11000
#递归函数--汉诺塔 问题
'''
算法：
    当只有一个盘子的时候，只需要从将A塔上的一个盘子移到C塔上。
    当A塔上有两个盘子是，先将A塔上的1号盘子（编号从上到下）移动到B塔上，再将A塔上的2号盘子移动的C塔上，最后将B塔上的小盘子移动到C塔上。
    当A塔上有3个盘子时，先将A塔上编号1至2的盘子（共2个）移动到B塔上（需借助C塔），然后将A塔上的3号最大的盘子移动到C塔，最后将B塔上的两个盘子借助A塔移动到C塔上。
    当A塔上有n个盘子是，先将A塔上编号1至n-1的盘子（共n-1个）移动到B塔上（借助C塔），然后将A塔上最大的n号盘子移动到C塔上，最后将B塔上的n-1个盘子借助A塔移动到C塔上。
    综上所述，除了只有一个盘子时不需要借助其他塔外，其余情况均一样（只是事件的复杂程度不一样）。
'''
print("递归函数--汉诺塔")


def move(*,buf,n,fromWhere,toWhere):
    print("第 %.3d 步:将 %.2d 号盘子 %s ----> %s " % (buf,n,fromWhere,toWhere))
    return buf + 1
    
def hanoi(*,n,buf=1,fromWhere='A',dependOn='B',toWhere='C'):
    if n == 1:
        buf = move(buf = buf,n=n,fromWhere=fromWhere,toWhere=toWhere)

    else:
        #将 n-1个盘子由 A 移动到 B 借助 C
        buf = hanoi(buf = buf,n=n-1, fromWhere=fromWhere, dependOn=toWhere, toWhere=dependOn)
        #将 第n个盘子由 A 移动到C
        buf = move(buf = buf, n=n,fromWhere=fromWhere,toWhere=toWhere)
        #将 n-1个盘子由 B 移动到 C 借助 A
        buf = hanoi(buf = buf,n=n-1, fromWhere=dependOn, dependOn=fromWhere, toWhere=toWhere)
    return buf
  
hanoi(n = 5,fromWhere='A',dependOn='B',toWhere='C')
