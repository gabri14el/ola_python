#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:34:54 2024

@author: gabrielsantos
"""

#inicializa nossa varável como lista
v = list()
v = []

#inicializa nossa variável como lista com valores iniciais

v = [1, 2, 3, 4]

#usar a palavra reservada len para saber tamanho da lista
print(len(v))

#iniciliza lista usando uma variável e outra lista (matriz!)
k = [v, [8, 9, 10]]

#imprime quantidade de elementos na lista
print(len(k))

#imprime elemento 0 da lista
print(k[0])

#imprime elmento 1 do elemento 0 da lista
print(k[0][1])

#deleta elemento da lista
del v[0]
print(v)
print(k)

#por que o valor foi também deletado de k?

#adiciona elemento na lista
v.append('new')
print(v)

#expande lista com valores de outra lista
v.extend('new')
print(v)
