#- **desafio 1:  Condicionais***

#***Sistema de Reservas de Hotel:***

#***Você foi contratado para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

#- *Cadastro de Cliente:*

#*O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

#- *Reservas de Quartos:*

##***"Simples", "Duplo" e "Luxo".***

#***Cada cliente deve escolher um quarto para sua estadia.
#O preço da diária varia conforme o tipo de quarto:
#Simples: R$ 100,00 por dia.
#Duplo: R$ 150,00 por dia.
#Luxo: R$ 250,00 por dia.***

#- ***Cálculo da Estadia:***

#***O usuário deve informar quantos dias cada cliente ficará no hotel.
#O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***
#Exemplo: 

# ***valor_cliente3 = preco_duplo * cliente3_dias***
#*Pagamento:*

#*O sistema deve exibir o valor total a ser pago por cada cliente.*
#*Regras Adicionais:
#**Utilize apenas variáveis, condicionais #(if, elif, else) e listas para resolver o desafio.***

#***O sistema não deve usar loops #(for, while) nem funções criadas por você.**
#O código deve considerar todos os casos possíveis de escolha dos clientes.*




dados = {

'cliente1':'idade1',
'cliente2':'idade2',
'cliente3':'idade3'
}
quartos_diaria = {

'Simples' : 100.00,
'Duplo' : 150.00, 
'Luxo' : 250.00,

}

cliente1 = input('Digite seu nome: ')
idade1 = int(input('Digite a sua idade: '))
dias_1 = int(input('Digite a quantidades de dias da estadia: '))

print(quartos_diaria)
estadia_1 = input('Digite o tipo do  quarto: ')
escolha1 = (quartos_diaria[estadia_1])

valor_1 = escolha1 * dias_1


print(cliente1)
print( valor_1)


cliente2 = input('Digite seu nome: ')
idade2 = int(input('Digite a sua idade: '))
dias_2 = int(input('Digite a quantidades de dias da estadia: '))

print(quartos_diaria)
estadia_2 = input('Digite o tipo do  quarto: ')
escolha2 = (quartos_diaria[estadia_2])

valor_2 = escolha2 * dias_2


print(cliente1, cliente2)
print(valor_1, valor_2)


cliente3 = input('Digite seu nome: ')
idade3 = int(input('Digite a sua idade: '))
dias_3 = int(input('Digite a quantidades de dias da estadia: '))

print(quartos_diaria)
estadia_3 = input('Digite o tipo do  quarto: ')
escolha3 = (quartos_diaria[estadia_3])

valor_3 = escolha3 * dias_3


print(cliente1, cliente2, cliente3)
print(valor_1, valor_2, valor_3)
