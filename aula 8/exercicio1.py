#EXERCÍCIOS 1: 
#Utilize condicionais

# 1* # Peça para o usuário digitar um número, verifique se um número é positivo, 

numero = int(input('digite um numero: '))
if numero > 0:
    print('Este numero é positivo')
if numero <= 0 :
    print('Esse numero não é positivo')

 # 2*# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.


idade = int(input('digite sua idade: '))
if idade >= 18:
    print('Voce pode votar')
if idade < 18:
    print('Não pode votar')

# 3*# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.


numero_qualquer = int(input('digite um numero: '))
print('Seu numero é: ')
if numero_qualquer % 2 == 0:
    print('par')
else :
    print('impar')



# 4 # Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))
print('Se seu numero fosse um trinagulo ele seria:')
if n1 == n2 and n1 == n3:
    print('equilátero')
if n1 == n2 or n1 == n3 and n2 == n3 or n3 == n1 and n1 != n2 or n2 != n3 or n3 != n1:
    print('isósceles') 
if n1 != n2 and n2 != n3 and n3 != n1:
    print('escaleno')

# 5*# Determine se um número é múltiplo de 5 e 7.

#um_numero = int(input('Digite um numero: '))
#if um_numero % 


# 6*# Verifique se um número é positivo e maior que 10

se_um_numero = int(input(' Mais uma vez, digite um numero: '))

if se_um_numero > 0 and se_um_numero >10 :
    print('seu um número é positivo e maior que 10')
else:
    print('seu um número não é positivo e maior que 10')

# 7*# Verifique se um número é divisível por 3 ou 5.

n560 = int(input('Já estou cansado de tanto numero. Escreva mais um numero: '))

if n560 % 3 == 0:
    print('numero divisivel por 3') 
if n560 % 5 == 0:
    print('numero divisivel por 5') 
if n560 % 5 == 0 and  n560 % 3 == 0:
    print('numero divisivel por 3 e 5') 
else:
    print('número não divisível por 3 e 5.')