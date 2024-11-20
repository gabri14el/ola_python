#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:34:54 2024

@author: gabrielsantos
"""


import math


#initialize with the name of operations
operations = ['Sum', 'Mul', 'Sub', 'Pow', 'Log10']




#iter over the operations, printing it names and indexes
num_operations = len(operations)
counter = 0
while(counter < num_operations):
    print(f"{counter}): {operations[counter]}")
    counter += 1
print('Type an operation number or a negative number to leave:')


#read the value from keyboard and cast it to int
op = int(input())


#calculator main loop, exiting when any another option is selected
while(op in list(range(len(operations)))):
    
    #print selected opration
    print(f'Selected operation: {operations[op]}')
    
    
    #read the operators
    print('Type the first operator: ')
    a = float(input())
    
    #if 4 is selected read only a operator
    if not op == 4:
        print('Type the second operator: ')
        b = float(input())
    
    #define string aux to print the result
    aux = '=======\nThe result is: {}\n======='
    
    #execute the operation
    if op == 0:
        print(aux.format(str(a+b)))
    elif op == 1:
        print(aux.format(str(a*b)))
    elif op == 2:
        print(aux.format(str(a-b)))
    elif op == 3: 
        print(aux.format(str(a**b)))
    elif op == 4:
        #verify if number is different from 0
        if a > 0:
            print(aux.format(str(math.log10(a))))
        else:
            print(f'Log not defined in {a}')
    
    #iter again over the operations, this time using a combination between for and enumerate
    for i, operation in enumerate(operations):
        print(f"{i}): {operation}")
    print('Type an operation number or a negative number to leave:')
    op = int(input())