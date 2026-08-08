import tkinter as tk
from tkinter import ttk

def conversao_button():
    valor = entrada_valor.get()
    conversao = valor * 5.5
    

janela = tk.Tk()
janela.title("SENAI - Sistemas")
janela.tk_setPalette(background="#dcdad5")

valor_label = tk.Label(janela, text="Valor da moeda:").grid(row=0, column=0, sticky="ns", padx=8, pady=8)

moeda_origem = tk.Label(janela, text="Moeda de Origem:").grid(row=1, column=0, sticky="ns", padx=8, pady=8)

moeda_destino = tk.Label(janela, text="Moeda de destino:").grid(row=2, column=0, sticky="ns", padx=8, pady=8)


entrada_valor= tk.Entry(janela, width=24, bg="lightgray")
entrada_valor.grid(row=0, column=1, sticky="ns", padx=8, pady=8)

m_origem = ttk.Combobox(janela, values=["BRL","USD", "EUR"], state="readonly", width=25)
m_origem.grid(row=1, column=1, sticky="ns", padx=5, pady=5)

m_destino = ttk.Combobox(janela, values=["BRL","USD", "EUR"], state="readonly", width=25)
m_destino.grid(row=2, column=1, sticky="ns", padx=5, pady=5)

button = tk.Button(janela, text="Converter", command=conversao_button, activebackground="blue", activeforeground="white")
button.grid(row=3, column=1, sticky="sn",padx=5, pady=5)



janela.mainloop()
