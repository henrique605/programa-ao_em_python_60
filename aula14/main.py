
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# O arquivo é automaticamente fechado após sair do bloco "with"
