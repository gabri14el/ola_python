#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:18:41 2024

@author: gabrielsantos
"""

varieties = {
    "tinto cao": "TC",
    "tinta francisca": "TF",
    "alicante": "AC",
    "alveralhao": "AV",
    "arinto": "AT",
    "bastardo": "BT",
    "boal": "BA",
    "cabernet franc": "CF",
    "cabernet sauvignon": "CS",
    "carignon noir": "CN",
    "cercial": "CC",
    "chardonnay": "CD",
    "codega": "CG",
    "codega do larinho": "CR",
    "cornifesto": "CT",
    "donzelinho": "DZ",
    "donzelinho branco": "DB",
    "donzelinho tinto": "DT",
    "esgana cao": "EC",
    "fernao pires": "FP",
    "folgasao": "FG",
    "gamay": "GM",
    "gouveio": "GV",
    "malvasia corada": "MC",
    "malvasia fina": "MF",
    "malvasia preta": "MP",
    "malvasia rei": "MR",
    "merlot": "ML",
    "moscatel galego": "MG",
    "moscatel galego roxo": "MX",
    "mourisco tinto": "MT",
    "pinot blanc": "PB",
    "rabigato": "RB",
    "rufete": "RF",
    "samarrinho": "SM",
    "sauvignon blanc": "SB",
    "sousao": "SS",
    "tinta amarela": "TA",
    "tinta barroca": "TB",
    "tinta femea": "TM",
    "tinta roriz": "TR",
    "touriga francesa": "TS",
    "touriga nacional": "TN",
    "viosinho": "VO"
}

#imprime chaves
print(varieties.keys())

#imprime valores
print(varieties.values())

#acessa um valor atraves de uma chave
print(varieties['alveralhao'])

#verifica se a chave rufete esta definida
print('rufete' in varieties)

#verifica se existe TR dentro de valores
print('TR' in varieties.values())

#outra forma de inicializar
person = dict(Nome='Sara',
          Idade=27,
          Documento=dict(cc='123456', nif='xxXXxx123', utente=None))

print(person)

#modifica chave idade
person['Idade'] = 40

print(person)

#cria chave e atribui valor 
person['cartaMotorista'] = False

print(person)

#modifica o valor
person['cartaMotorista'] = True

print(person)

#busca chave e se chave nao esta definida, retorna valor padrao
print(person.get('Morada', 'Morada nao definida'))

#deleta chave
person.pop('cartaMotorista')

print(person)

#acessa dicionario dentro de dicionario
print(person['Documento']['nif'])

