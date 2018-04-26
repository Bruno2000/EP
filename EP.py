#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 07:36:47 2018

@author: rbalkins
"""

estoque = {}
i = 0
while i == 0:
    print ("Controle de estoque")
    print ("0 - sair")
    print ("1 - adicionar item")
    print ("2 - remover item")
    print ("3 - alterar item")
    print ("4 - imprimir estoque")
    a = int(input("Faça sua escolha: "))
    if a == 0:
        print ("Até mais")
        i+=1
    elif a == 1:
        b = str(input("Nome do produto: "))
        if b in estoque:
            print ("Produto já está cadastrado.")
        else:
            c = int(input("Quantidade inicial: "))
            while c < 0:
                print("A quantidade inicial não pode ser negativa.")
                c = int(input("Quantidade inicial: "))
            else:
                estoque[b] = {"quantidade":c}
    elif a == 2:
        d = str(input("Nome do produto: "))
        if d in estoque:
            del estoque[d]
        else:
            print("Elemento não encontrado")
    elif a == 3:
        e = str(input("Nome do produto: "))
        if e not in estoque:
            print ("Elemento não encontrado")
        else:
            f = int(input("Quantidade: "))
            for l in estoque:
                for m in estoque[l]:
                    estoque[l][m] += f
            print ("Novo estoque de {0}: {1}".format(e, estoque[l][m]))
    elif a == 4:
        for k in estoque:
            for j in estoque[k]:
                print ("{0}: {1}".format(k, estoque[k][j]))
    else:
        print ("Comando não existente")
