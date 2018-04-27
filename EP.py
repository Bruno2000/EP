#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 07:36:47 2018

@author: rbalkins
"""
import json
import os.path


if os.path.exists ("dados.json") == False:
    with open("dados.json", "w") as arquivo:
        arquivo.write ("{}")
with open("dados.json", "r") as arquivo:
    estoque = json.loads(arquivo.read())
    


lojas = {}
estoque = {}
i = 0
w = 0
while w == 0:
    print ("\nCentral do estoque de lojas")
    print ("0 - sair")
    print ("1 - adicionar loja")
    print ("2 - remover loja")
    print ("3 - configurar estoque")
    x = int(input("Faça sua escolha: "))
    if x == 0:
        print ("Até mais")
        w+=1
    elif x == 1:
        y = str(input("Nome da loja: "))
        if y in lojas:
            print ("Loja já cadastrada.")
        else:
            lojas[y] = estoque
    elif x == 2:
        z = str(input("Nome da loja: "))
        if z in lojas:
            del lojas[z]
        else:
            print ("Loja não existente")
    elif x == 3:
        j = str(input("Qual loja deseja configurar o estoque: "))
        if j not in lojas:
            print ("Loja não cadastrada")
        else:
            lojas[j]
            while i == 0:
                print ("\nControle de estoque")
                print ("0 - voltar")
                print ("1 - adicionar item")
                print ("2 - remover item")
                print ("3 - alterar item")
                print ("4 - imprimir estoque")
                print ("5 - controle dos preços")
                print ("6 - produtos em falta")
                print ("7 - valor monetário do estoque")
                a = int(input("Faça sua escolha: "))
                if a == 0:
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
                            estoque[l]["quantidade"] += f
                        print ("Novo estoque de {0}: {1}".format(e, estoque[l]["quantidade"]))
                elif a == 4:
                    for k in estoque:
                        print ("{0}: {1}".format(k, estoque[k]["quantidade"]))
                        print (lojas)
                elif a == 5:
                    o = 0
                    while o == 0:
                        print ("0 - voltar")
                        print ("1 - manusear preço")
                        g = int(input("Faça sua escolha: "))
                        if g == 0:
                            o+=1
                        elif g == 1:
                            h = str(input("Adicionar ou alterar preço a qual produto: "))
                            n = float(input("Preço: "))
                            estoque[h]["preco"]=n
                        else:
                            print("Comando não existente")
                elif a == 6:
                    lista_faltas = []
                    lista_sem_faltas = []
                    for r in estoque:
                        if estoque[r]["quantidade"] <= 0:
                            print(r)
                        else:
                            lista_sem_faltas+=estoque[r]
                elif a == 7:
                    valor_monetario = 0
                    for t in estoque:
                        valor_monetario+=estoque[t]["preco"]*estoque[t]["quantidade"]
                    print ("O valor monetário total do estoque é de {0}".format(valor_monetario))
                        
                else:
                    print ("Comando não existente")
    else:
        print ("Comando não existente")
        
original = json.dumps(estoque, sort_keys=True)
with open ("dados.json","w") as arquivo:
    arquivo.write (original)