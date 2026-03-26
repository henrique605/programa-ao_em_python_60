## Desafio 2

# Você é um analista de dados, e decidiu trocar de emprego.

# Utilize a media, moda, mediana e o desvio padrão para decidir qual empresa faz sentido para você:

# Justificar por que decidiu por essa empresa.

# ***Verifique isso através dos salários:***

empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

import statistics
print()
print('MEDIA')
media1 = statistics.mean(empresa1)
print(media1)
media2 = statistics.mean(empresa2)
print(media2)
media3 = statistics.mean(empresa3)
print(media3)
media4 = statistics.mean(empresa4)
print(media4)

lista_media = [media1,media2,media3,media4]

print()
print('MODA')
moda1 = statistics.mode(empresa1)
print(moda1)
moda2 = statistics.mode(empresa2)
print(moda2)
moda3 = statistics.mode(empresa3)
print(moda3)
moda4 = statistics.mode(empresa4)
print(moda4)

lista_moda = [moda1,moda2,moda3,moda4]

print()
print('DEVIO PADRÃO')


desvio1 = statistics.stdev(empresa1)
print(desvio1)
desvio2 = statistics.stdev(empresa2)
print(desvio2)
desvio3 = statistics.stdev(empresa3)
print(desvio3)
desvio4 = statistics.stdev(empresa4)
print(desvio4)

lista_desvio = [desvio1,desvio2,desvio3,desvio4]

maior_media = max(lista_media)
maior_moda = max(lista_moda)
menor_desvio = min(lista_desvio)

lista_melhor_empresa = [maior_media, maior_moda, menor_desvio]

print()
print('melhor_emrpesa')
p1 = lista_media.index(maior_media)
p2 = lista_moda.index(maior_moda)
p3 = lista_desvio.index(menor_desvio)
print('melhor media: ', p1, maior_media)
print('melhor moda: ', p2, maior_moda)
print('menor desvio: ', p3, menor_desvio)