import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.tk_setPalette(background="#dcdad5")

estilo = ttk.Style()
estilo.theme_use('clam')



def botao_enviar():
    messagebox.showinfo(
        "Cadastro",
        "Você concluiu o cadastro!!"
    )

def entry_nome():
    nome = entrada_nome.get()
    messagebox.showinfo("Informação", nome)


imagem_label = tk.PhotoImage(file="perfil-de-usuario.png").subsample(3, 3)
label_foto = tk.Label(root, image=imagem_label, relief=tk.RAISED).grid(row=0, column=0, rowspan=5, sticky="ns", padx=5, pady=5)

label_nome = tk.Label(root,
    text="Nome:",
    width=2,
    height=2
    ).grid(row=0, column=1,  sticky="ew", padx=5, pady=5)

label_genero = tk.Label(root, text="Gênero:", width=5, height=2).grid(row=1, column=1, sticky="ns", padx=5, pady=5)

label_olhos = tk.Label(root, text="Cor dos olhos:", width=10,height=2).grid(row=2, column=1, rowspan=1, sticky="ns", padx=5, pady=5)

label_altura = tk.Label(root, text="Altura (cm):", width=8, height=2).grid(row=3, column=1, rowspan=1, sticky="ns", padx=5, pady=5)

label_peso = tk.Label(root, text="Peso (kg):", width=8, height=3).grid(row=4, column=1, rowspan=1, sticky="ns", padx=5, pady=5)


entrada_nome = tk.Entry(root, width=24, bg="lightgray")
entrada_nome.grid(row=0, column=2, padx=5, pady=5)

entrada_genero = ttk.Combobox(root, values= ["Masculino", "Feminino"],state="readonly",width= 22)
entrada_genero.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

entrada_olhos = ttk.Combobox(root, values= ["Castanhos", "Preto", "Azul"],state="readonly", width= 22)
entrada_olhos.grid(row = 2, column=2, sticky="ew", padx=5, pady=5)

entrada_altura = tk.Entry(root, width=24, bg="lightgray")
entrada_altura.grid(row=3, column=2, padx=5, pady=5)

entrada_peso = tk.Entry(root, width=24, bg="lightgray")
entrada_peso.grid(row=4, column=2, padx=5, pady=5)

button = tk.Button(root, text="Enviar", command=entry_nome, activebackground="blue", activeforeground="white")
button.grid(row=5, column=2, sticky="e",padx=5, pady=5)


root.mainloop()

#"activebackground" serve para mudar a cor do botão quando pressionado
#"activeforeground" muda a cor do texto do botão ao ser pressionado
# bg ou background: Altera a cor de fundo da caixa de texto.
# fg ou foreground: Altera a cor do texto digitado.