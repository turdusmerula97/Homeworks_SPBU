#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Задание: переписать вычисление n-ного члена последовательности Фибоначчи с помощью рекурсии.
"""

def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

