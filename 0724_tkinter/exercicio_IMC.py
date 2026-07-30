import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

label_1 = tk.Label(root, text="Peso(Kg)")
label_1.pack(expand=False)

def enter_pressionado(event):
    label_1.config(text=event.widget.get())

entry_peso = tk.Entry(root)

entry_peso.bind("<Return>", enter_pressionado)
entry_peso.pack()

label_2 = tk.Label(root, text="Altura(m)")
label_2.pack(expand=False)

def enter_pressionado(event):
    label_1.config(text=event.widget.get())

entry_altura = tk.Entry(root)
entry_altura.insert(0, "Digite sua altura")
entry_altura.bind("<Return>", enter_pressionado)
entry_altura.pack()




def button_command():
    peso = label_1
    altura = label_2
    IMC = (label_1 / label_2)
    messagebox.showinfo(
        "IMC",
        "Você clicou no botão!"
    )

button = tk.Button(
    root,
    text="Calcular IMC",
    command=button_command
)
button.pack()
root.mainloop()