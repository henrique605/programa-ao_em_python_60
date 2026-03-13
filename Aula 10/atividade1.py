## ***ATIVIDADE 1***

# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.

n1 = 0

while n1 <=1000: 
    print(n1)
    n1 = n1 + 1



# 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

dez_pessoas = []

x = 1 

while x <=10:
    print('pessoa: ', x)
    pessoa = input('Digite o nome da pessoa: ')
    dez_pessoas.append(pessoa)
    print('pessoas: ',dez_pessoas)
    x = x + 1


