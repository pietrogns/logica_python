import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

def selecao_mudou(evento):
    sel = evento.widget.curselection()
    if sel:
        idx = sel[0]
        label.config(
            text=f"{evento.widget.get(idx)} selecionado!")
#get(indice) = retorna o item na posição especificada.
#curselection() = Retorna uma tupla com os índices dos itens selecionados.

listbox = tk.Listbox(root)
for item in ["Primeiro", "Segundo", "Terceiro"]:
    listbox.insert(tk.END, item)
#insert(pos, item) = Adiciona um item na posição indicada. Use tk.END para o final.
listbox.bind("<<ListboxSelect>>", selecao_mudou)
listbox.pack(expand=True)

label = tk.Label(root, text="Primeiro selecioado!")
label.pack()

root.mainloop()
