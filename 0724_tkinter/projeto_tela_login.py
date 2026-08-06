import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

label_1 = tk.Label(root, 
                text="Faça seu login",
                font=("font", 30))
label_1.pack()

minha_imagem = tk.PhotoImage(file="usuario.png").subsample (9, 9)
label = tk.Label(root, image=minha_imagem, relief=tk.RAISED)
label.pack()










root.mainloop()
#relief=tk.RAISED - serve para deixar as bordas da imagem rodandas

import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

label_1 = tk.Label(root, 
                text="Faça seu login",
                font=("font", 30))
label_1.pack()

minha_imagem = tk.PhotoImage(file="usuario.png").subsample (9, 9)
label = tk.Label(root, image=minha_imagem, relief=tk.RAISED)
label.pack()

tk.Label(root, text="Senha").pack(anchor="w", padx=30)
password_entry = tk.Entry(root)
password_entry.pack()

tk.Button(root, text= "Entrar", width= 18 )





#fg serve para especificar a cor
root.mainloop()