import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")


imagem_label = tk.PhotoImage(file="usuario.png").subsample(15,15)
label_foto = tk.Label(root, image=imagem_label, relief=tk.RAISED).grid(row=0, column=0, rowspan=5, sticky="ns", padx=5, pady=5)

label_nome = tk.Label(root,
    text="Nome:",
    width=5,
    height=5
    ).grid(row=0, column=1,  sticky="ew", padx=5, pady=5)

label_genero = tk.Label(root,
                        text="Gênero:", 
                        width=5,
                        height=5
                        ).grid(row=1, column=1, sticky="ns", padx=5, pady=5)

label_olhos = tk.Label(root,
                       text="Cor dos olhos:", 
                       width=10,
                       height=5
                       ).grid(row=2, column=1, rowspan=1, sticky="ns", padx=5, pady=5)

label_altura = tk.Label(root,
                        text="Altura (cm):", 
                        width=10,
                        height=5
                        ).grid(row=3, column=1, rowspan=1, sticky="ns", padx=5, pady=5)

label_peso = tk.Label(root,
                      text="Peso (kg):",
                        width=8,
                        height=5
                        ).grid(row=4, column=1, rowspan=1, sticky="ns", padx=5, pady=5)


entrada_nome = tk.Entry(root, width=25)
entrada_nome.grid(row=0, column=2, padx=10, pady=10)

entrada_genero = tk.Entry(root, width=25)
entrada_genero.grid(row = 1, column=2, padx=10, pady=10)

entrada_olhos = ttk.Combobox(root, 
                             values= ["Castanhos", "Preto", "Azul"],
                             state="readonly",
                             width= 25)
entrada_olhos.grid(row = 2, column=2, padx=10, pady=10)

entrada_altura = tk.Entry(root, width=25)
entrada_altura.grid(row=3, column=2, padx=10, pady=10)

entrada_peso = tk.Entry(root, width=25)
entrada_peso.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()