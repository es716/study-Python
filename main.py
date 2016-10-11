#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#==============================================


from test import my_abs,power,add_end,calc,person,person1,person2



names = [1, 2, 3]

print(my_abs(-90))

print (power(25, 5))
print (power(25))
print (add_end())
print (add_end())
print (calc(1,2,3))
print (calc())
print (calc(*names))
person('es',16)
person('es',16,country='China')
person('es',16,country='China',city='Beijing')
person1('es',16,city='Beijing',job = 'studence')
#person1('Jack', 24, 'Beijing', 'Engineer')
person2('es',16,city='Beijing',job = 'studence')
person2('es',16)


'''
获取网页
import urllib.request
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')

html = getHtml("https://movie.douban.com/")

print (html)
'''
