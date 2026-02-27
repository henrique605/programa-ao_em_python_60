print('sistema de verificaçao de medias')

nome = input('digite o nome do aluno:')

n1 = float(input('digite sua nota'))
n2 = float(input('digite sua nota'))
n3 = float(input('digite sua nota'))
print('***'*15)
print('media do aluno', nome)
media = (n1+n2+n3)/3
print("a media do aluno",  nome)
print(media)

aprovada = media >= 7
recuperaçao = media >5 and media <7 
reprovada = media <5 

print(f'''''         
SITUAÇAO DA ALUNA {nome}
aprovada - {aprovada}
reprovada {reprovada}
recuperaçao  {recuperaçao}
      ''''')