# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:48:19 2020

@author: douzi
"""

def factor(num):
    i = 1
    res = 0
    while i < num:
        if num % i == 0:
            res += i
        i = i + 1
    return res


def main():
    while True:
        n = int(input("输入n:"))
        print(factor(n))

if __name__=='__main__':
    main()