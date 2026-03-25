## Exercícios com funções:

# variáveis locais, globais e parâmetros

# ***1*** 

# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***

# def comparar():
    




# ***2***

# ***CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***

a = float(input('Numero 1: ' ))
b = float(input('Numero 2: ' ))
c = float(input('Numero 3: ' ))

def multiplicaçao(a,b,c):
    return a*b*c
resultado = multiplicaçao(a,b,c)

print(resultado)

# ***3***

# ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

# elevado = float(input('Numero 4: ' ))

# def multiplicaçao(a,b,c):
#     return a*
# resultado = multiplicaçao(a,b,c)

# print(resultado)




# ***4***

# ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***

idade = int(input('digite sua idade: '))


def mmaioridade(idade):
    return 'o exercito te espera...'

if idade == 18:
    print(mmaioridade(idade))

# ***5***

# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***


def sua(idade):
    return 'Sua idade é'  idade


print(sua(idade))








# ***6***

# ***DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.**

copa98 = input('o Brasil ganhou a copa de 98?: ')


def ganhou(copa98):
    return 'O Brasil ganhou.'

if copa98 == 'sim':
    print(ganhou(copa98))