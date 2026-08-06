import tkinter as tk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")


imagem_label = tk.PhotoImage(file="usuario.png").subsample(10,10)
label_foto = tk.Label(root, image=imagem_label, relief=tk.RAISED).grid(row=0, column=0, rowspan=5, sticky="ns", padx=5, pady=5)

label_nome = tk.Label(root,
    text="Nome:",
    width=5,
    height=5
    ).grid(row=0, column=1,  sticky="ew", padx=5, pady=5)

label_genero = tk.Label(root,text="Gênero:", width=5,height=5).grid(row=1, column=1, sticky="ns", padx=5, pady=5)

label_olhos = tk.Label(root,text="Cor dos olhos:", width=10,height=5).grid(row=2, column=1, rowspan=1, sticky="ns", padx=5, pady=5)

label_altura = tk.Label(root,text="Altura (cm):", width=10,height=5).grid(row=3, column=1, rowspan=1, sticky="ns", padx=5, pady=5)

label_peso = tk.Label(root,text="Peso (kg):", width=8,height=5).grid(row=4, column=1, rowspan=1, sticky="ns", padx=5, pady=5)



root.mainloop()