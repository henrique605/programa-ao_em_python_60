import random


def atividade1():
    x  =  random.randint(5,10)
    return x

def atividade2():
    x  =  random.randint(1,10)
    y  =  random.randint(1,10)
    z  =  random.randint(1,10)
    return x, y, z

def atividade3():
    x = random.randrange(10,30)
    return x

def atividade4():
    for x in range(10, 0, -1):
        print(x)
    return 'fogo'

def atividade5():
    x = int(input('insira um número inteiro positivo: '))
    y = x+1
    l = []
    if x > 0:
        for s in range(0, y, 2):
            l.append(s)
    return sum(l)

def atividade6():
    x = int(input('Insira um numero: '))
    for s in range(1, 11):
        print(s*x)
    return ' '

def atividade7():
    for s in range(99, 0, -2):
        print(s)
    return ' '