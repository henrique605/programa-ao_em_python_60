#***EXERCÍCIOS com match/ case:*** 

#***1: Verificando se o número é par ou ímpar***

n1 = int(input('digite um numero: '))

match n1 % 2:
    case 0:
        print('Número par')
    case _:
        print('Número ímpar')



#***2: Verificando se um número é positivo, negativo ou zero***

n2 = int(input('Vamos lá mais uma vez, Digite outro número: '))

match n2 :
    case n2 if n2 > 0:
        print('Número positivo')
    case 0:
        print('É zero')
    case n2 if n2 < 0:
        print('Número negativo')



#***3: Verificando se uma string é vazia ou não***

x = input('')
match x:
    case '':
        print("vazia")
    case _: 
        print('preenchida') 


#***4: Verificando se um número é maior, menor ou igual a 10***

n3 = int(input('Vamos lá mais uma vez, Digite outro número: '))

match n3 :
    case n3 if n3 > 10:
        print('Número maior que 10')
    case 10:
        print('É dez')
    case n3 if n3 < 10:
        print('Número menor que dez')



#***5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)***


idade = int(input('Digite sua idade: '))

match idade:
    case idade if idade < 0 or idade < 13:
        print('Criança')
    case idade if idade > 14 or idade < 18:
        print('adolescente')
    case idade if idade > 17 or idade < 35:
        print('jovem')
    case idade if idade > 34 or idade < 64:
        print('adulto')
    case idade if idade > 63 :
        print('idoso')
