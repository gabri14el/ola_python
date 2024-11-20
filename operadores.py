#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:34:54 2024

@author: gabrielsantos
"""

#importa biblioteca math
import math


#inicializa variaveis
a = 2 
b = 51
c = 1 + 2j

m = [1, 2, 3]
n = [4, 5]


aux = a > 2
print(aux)
print(a > 2)

#verifica se a eh menor que 2 e 51 nao eh par
print(a == 2 and not 51 % 2 == 0)
print(a == 2 and 51 % 2 != 0)

#imprime o valor da concatenacao de m e n
print(m + n)

#tenta operacao de subtracao com listas
aux = m - n

#alguns outros operadores
print(a ** b)
print(c ** 2)


#biblioteca math
print(math.sqrt(c))
print(math.sqrt(b))
print(math.log(b))
print(math.sin(a))