#!/usr/bin/env python
# coding: utf-8

""" Задание: написать класс связанных списков. """


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    '''
    элемент связанного списка, содержит информацию о значении 
    и о следующем элементе (которого нет, если текущий элемент - последний)
    '''

class LinkedList: 
    
    def __init__(self):
        self.first_node = None
        
    def add_node(self, num): # добавление элемента к LL
        added_node = Node(num)
        added_node.next_node = self.first_node
        self.first_node = added_node
        
    def remove_first_node(self): # удаление первого элемента LL
        if(self.first_node == None):
            return
 
        self.first_node = self.first_node.next_node
        
    def delete_node(self, num): # удаление конкретного элемента LL (value == num)
 
        if current_node.value == num:
            current_node = self.first_node
            self.remove_first_node()
            return
 
        while(current_node != None and current_node.next_node.value != num):
            current_node = current_node.next_node
 
        if current_node == None:
            return
        else:
            current_node.next_node = current_node.next_node.next_node
            
    def __len__(self): # длина LL
        length = 0
        if(self.first_node):
            current_node = self.first_node
            while(current_node):
                length = length + 1
                current_node = current_node.next_node
            return length
        else:
            return 0
    
    def print_List(self): # выводит список на экран
        current_node = self.first_node
        while(current_node):
            print(current_node.value)
            current_node = current_node.next_node
        
llist = LinkedList()
llist.add_node(1)
llist.add_node(3)
llist.add_node(5)
print(llist.__len__())
llist.print_List()
llist.delete_node(3)
llist.print_List()
llist.add_node(22)
llist.remove_first_node
llist.print_List()

