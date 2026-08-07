import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

def selecao_mudou(evento):
    label.config(text=f"{evento.widget.get()} selecionado!")

combobox = ttk.Combobox(root, values=["Primeiro", "Segundo", "Terceiro"])
#values = lista de opções dispo para o usuário selecionar.
combobox.set("Primeiro")
#set() = define o valor exibido inicialmente no campo.
combobox.bind("<<ComboboxSelected>>", selecao_mudou)
#bind() = Associa o evento <<ComboboxSelected>> a uma função de callback. Disparado quando se seleciona um item.
combobox.pack()


label = tk.Label(root, text="Primeiro selecionado!")
label.pack()

root.mainloop()

