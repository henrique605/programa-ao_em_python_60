# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

n1 = input('Digite um numero: ')

try:
    n1 = int(n1)
    print(n1)
except ValueError:
    print('o numero não é inteiro.')



# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

numero1 = float(input('digite mais um numero: '))
numero2 = float(input('digite mais um numero: '))

try: 
    print(numero1/numero2)
except ZeroDivisionError:
    print('Divisaõ não pode ser dividida por zero.')


# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

l = [1,2,3,4,5,6]

try:
    print(l[7])
except IndexError:
    print('Posição na lista não existe.')