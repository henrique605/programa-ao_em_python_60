
import os
import shutil


# **exercício 1: Criar e ler um Arquivo**

with open("notas.txt", "w") as arquivo:
    arquivo.write("Aprendendo manipulação de arquivos!")


with open("notas.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(f"Conteúdo do arquivo: {conteudo}")

# **Exemplo 2: Cria um Diretório**

os.makedirs("meu_projeto", exist_ok=True)
print("Diretório criado com sucesso!")



# **Exercício 3: Renomear um Diretório**

os.rename("meu_projeto", "projeto_final")
print("Diretório renomeado!")

# **Exercício 4:  Listar Arquivos em um Diretório** 

arquivos = os.listdir(".") # "." refere-se ao diretório atual
for item in arquivos:
    print(f"Item encontrado: {item}")


# **Exercício 5:  Copiar Arquivos em um Diretório**

shutil.copy("notas.txt", "notas_backup.txt")
print("Arquivo copiado!")


# **Exercício 6:  Remover**

os.remove("notas_backup.txt")

# Para remover um diretório e tudo dentro dele
shutil.rmtree("projeto_final")
print("Remoções concluídas!")