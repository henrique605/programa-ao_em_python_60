import tkinter as tk



def mostrar():
    dado =  nome.get()
    dado1 = idade.get()
    dado2 = email.get()
    dado3 = endereço.get()
    dado4 = cep.get()
    dado5 = cidade.get()
    dado6 = celular.get()
    dado7 = curso.get()
    print(dado)
    print(dado1)
    print(dado2)
    print(dado3)
    print(dado4)
    print(dado5)
    print(dado6)
    print(dado7)


janela  =  tk.Tk()
janela.geometry('1700x750')
janela.configure(bg = 'white')
# janela.iconbitmap('x.ico')


texto = tk.Label(janela, text = 'Formulario, cadastro de clientes', font=('arial', 25), bg = 'white')
texto.pack(pady=90)



texto = tk.Label(janela, text = 'Digite seu nome completo:', font=('arial', 15), bg = 'white')
texto.pack()
nome  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
nome.pack()


texto = tk.Label(janela, text = 'Digite sua idade:', font=('arial', 15), bg = 'white')
texto.pack()
idade = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
idade.pack()

texto = tk.Label(janela, text = 'Digite seu email:', font=('arial', 15), bg = 'white')
texto.pack()
email  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
email.pack()

texto = tk.Label(janela, text = 'Digite seu endereço:', font=('arial', 15), bg = 'white')
texto.pack()
endereço  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
endereço.pack()

texto = tk.Label(janela, text = 'Digite seu CEP:', font=('arial', 15), bg = 'white')
texto.pack()
cep  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
cep.pack()

texto = tk.Label(janela, text = 'Digite sua cidade:', font=('arial', 15), bg = 'white')
texto.pack()
cidade  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
cidade.pack()

texto = tk.Label(janela, text = 'Digite seu celular:', font=('arial', 15), bg = 'white')
texto.pack()
celular  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
celular.pack()

texto = tk.Label(janela, text = 'Digite seu curso:', font=('arial', 15), bg = 'white')
texto.pack()
curso  = tk.Entry(janela, font=('arial', 20), bg = '#e5e5e5')
curso.pack()


botao = tk.Button(janela, text="Enviar", command=mostrar)
botao.pack(pady=5)

janela.mainloop()

