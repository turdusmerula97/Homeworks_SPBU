#!/usr/bin/env python
# coding: utf-8

"""
Задание: написать функцию, которая принимает как аргумент
алфавит последовательности, а возвращает
функцию получения статистики встречаемости символов в последовательности
"""

def creation_func_symbols(alphabet: str): # принимает последовательность типа "ABCabc12345"
    
    created_alphabet = set(alphabet)
    alph_dict = dict(zip(created_alphabet, [0]* len(alphabet))) #разделение последовательности
    
    def alphabet_percentage(sequence: str):
        
        symbols = set(sequence)
        if not (symbols <= created_alphabet):
            raise Exception("Sequence has symbols, which are not included in the alphabet!")
            
        for symbol in sequence:
            alph_dict[symbol] += 1 / len(sequence)
        for symbol, percentage in alph_dict.items():
            print(f'{symbol}: {percentage / len(sequence):.2%}')
            
    return alphabet_percentage



count_aminoacids = creation_func_symbols("ABCDEFGHIKLMNPQRSTUVWXYZ")
count_aminoacids("KHAMYPGIMWWPCLECMPANCYMGANMGKCKCAVWWPPFNIRWTMPMNCG")





