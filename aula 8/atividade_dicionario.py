## Desafio 1 #Crie um e-commerce com a estrutura de dicionários.#Produtos:  Livros, tablets e fones de ouvido#As ações: #Comprar
#Pagar  #mostra o valor da compra
 
e_commerce = { 

'livros': { 'Dom Casmurro':20.00, 'Harry Potter':30.00, 'Senhor dos Aneis':10.00},
'tablets': {'Samsung': 1000.00, 'Intel': 200.00, 'Multilaser': 300.00, },
'fones de ouvido':{ 'JBL': 100.00, 'Apple':500.00,'Samsung': 80.00,}

}

carrinho = []
valores = []

print('livros', 'tablets', 'fones de ouvido')
s1 = input('digite qual secao:')
print(e_commerce[s1])
p1 = input('digite qual produto:')
valor_p1 = (e_commerce[s1][p1])
carrinho.append(p1)
valores.append(valor_p1)
print(carrinho)
print('R$', valores)


print('livros', 'tablets', 'fones de ouvido')
s2 = input('digite qual secao:')
print(e_commerce[s2])
p2 = input('digite qual produto:')
valor_p2 = (e_commerce[s2][p2])
carrinho.append(p2)
valores.append(valor_p2)
print(carrinho)
print('R$', valores)
print('TOTAL: ' ,sum(valores))