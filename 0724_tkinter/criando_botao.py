#1° defina a função: crie uma função que será executada ao clicar.
#2° Vincule com command (passe o nome da função(sem parênteses) ao botão)
#3° Use "messagebox" para feedback ao usuário




import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

def button_command():
    messagebox.showinfo(
        "Informação",
        "Você clicou no botão!"
    )

def button_command2():
    messagebox.showinfo(
        "Botão 2",
        "Você clicou no botão 2!"
    )

def button_command3():
    messagebox.showinfo(
        "Mais um botão"
        "Perfeito! você conseguiu clicar!!"
    )

button = tk.Button(
    root,
    text="Clique aqui",
    command=button_command
)

button2 = tk.Button(
    root,
    text="Clique no botão 2!",
    command=button_command2
)

button3 = tk.Button(
    root,
    text="outro botão",
    command=button_command3
)

button.pack()
button2.pack()
button3.pack()

root.mainloop()