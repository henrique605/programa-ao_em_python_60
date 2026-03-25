## ***ATIVIDADE 2***# Crie um sistema de notas alunos, com as seguintes operações:# ***Utilize While ou for***#  **Sistema de notas de alunos**# - ***Visão do professor***# - Acesso a conta com condicionais# - 3 chances de acessar o sistema# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)# # - Inserir notas (se Senha correta)# # - Fazer a média# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***# ***IMPORTANTE:***# - Ao finalizar o código, insira na borda do script, no última linha:# input(’Digite enter para sair’)
sistema_de_notas = {
    'alunos': [],'medias': [],
    'login': 'fernando01',
    'senha':'abc'}
tentativas = 3
while tentativas > 0:
    login_acesso = input('Insira o login de acesso: ')
    senha_acesso = input('Insira a senha: ')
    if login_acesso == sistema_de_notas['login'] and senha_acesso == sistema_de_notas['senha']:
        print('Acesso concedido!!')
        print( 'Sistema de notas' )
        aluno = input('Digite o nome do aluno que deseja lançar nota: ')
        sistema_de_notas['alunos'].append(aluno)
        n1 = float(input('Digite a nota 1: '))
        n2 = float(input('Digite a nota 2: '))
        n3 = float(input('Digite a nota 3: '))
        media_aluno = round((n1+n2+n3)/3, 2)
        print('Media: ', media_aluno)
        print(sistema_de_notas['alunos'])
        break
    else:
        print('acesso negado')
        tentativas = tentativas - 1
        print('Voce tem:', tentativas, 'tentativas')
else: 
    print('conta bloqueada')
sair = input('Digite enter para sair: ')