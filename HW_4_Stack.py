#!/usr/bin/env python
# coding: utf-8

"""
Задание: написать класс очереди и стека,
используя внутри только списки.
"""

class Queue:

def __init__(self):
    self.queue_list = []

def add_to_queue(self, num): # добавление элемента в очередь
    self.queue_list.append(num)
    
def __len__(self): # возвращает длину очереди
    return len(self.queue_list)

def delete_from_queue(self): # удаляет первый (и так далее) элемент очереди
    if len(self):
        return self.queue_list.pop()
    else:
        raise IndexError("No elements in the queue.")
        

class Stack:

def __init__(self):
    self.stack_list = []
    
def push(self, num): # добавление элемента в стэк
    self.stack_list.append(num)
    
def __len__(self): #  возвращает длину стэка
    return len(self.stack_list)

def pop(self): # удаляет верхний элемент стэка
    if len(self):
        return self.stack_list.pop()
    else:
        raise IndexError("No elements in the stack.")

