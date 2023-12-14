#!/usr/bin/env python
# coding: utf-8


"""
Используя наборы символов из пакета string написать функцию, 
которая получает на вход строку и возвращает строку, 
в которой все буквы латинского алфавита из исходной строки преобразованы в заглавные символы. 
Использовать функции стандартной библиотеки upper() и find() нельзя.

Добавить к предыдущему заданию функцию с преобразованием всех символов в прописные 
и функцию с отражением (все заглавные становятся прописными и наоборот), минимально дублируя код. 
Использовать функции стандартной библиотеки lower() и find() нельзя.
"""

import string

def to_upper(string_x): # замена на заглавные
    trans_dict = str.maketrans(string.ascii_lowercase, string.ascii_uppercase) # создание словаря для пакетной замены символов
    string_x_trans = string_x.translate(trans_dict) # непосредственно пакетная замена
    return string_x_trans

def to_lower(string_x): # замена на строчные
    trans_dict = str.maketrans(string.ascii_uppercase, string.ascii_lowercase)
    string_x_trans = string_x.translate(trans_dict)
    return string_x_trans

def reflection(string_x): # функция замены заглавных на прописные и наоборот
    trans_dict = str.maketrans(string.ascii_uppercase + string.ascii_lowercase, string.ascii_lowercase + string.ascii_uppercase)
    string_x_trans = string_x.translate(trans_dict)
    return string_x_trans

print(to_upper("troglodytes"))
print(to_lower("TROGLODYTES"))
print(reflection("TrOgLoDyTeS"))

