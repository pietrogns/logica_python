import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

def enter_pressionado(event):
    label.config(text=event.widget.get())
#get() = retorna o conteúdo atual do campo.

entry = tk.Entry(root)
entry.bind("<Return>", enter_pressionado)
entry.pack()
#bind() = captura eventos como <Return> (tecla Enter).

label = tk.Label(root, text="Demonstração!")
label.pack()


root.mainloop()
