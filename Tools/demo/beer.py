#!/usr/bin/env python3

"""
A Python version of the classic "bottles of beer on the wall" programming
example.

By Guido van Rossum, demystified after a version by Fredrik Lundh.
"""

import sys   #import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。

n = 100
if sys.argv[1:]:      #sys.argv其实可以看作是一个列表 
    n = int(sys.argv[1])

def bottle(n):
    if n == 0: return "no more bottles of beer"
    if n == 1: return "one bottle of beer"
    return str(n) + " bottles of beer"

for i in range(n, 0, -1):
    print(bottle(i), "on the wall,")
    print(bottle(i) + ".")
    print("Take one down, pass it around,")
    print(bottle(i-1), "on the wall.")
