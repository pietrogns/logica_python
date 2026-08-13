
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

TAXAS = {
    "BRL": {"BRL": 1.0, "USD": 0.18, "EUR": 0.16},
    "USD": {"BRL": 5.5, "USD": 1.0, "EUR": 0.91},
    "EUR": {"BRL": 6.0, "USD": 1.1, "EUR": 1.0},
}


def conversao_button():
    try:
        valor = float(entrada_valor.get())
        de = combo_origem.get()
        para = combo_destino.get()

        resultado = valor * TAXAS[de][para]

        resultado_label.config(
            text=f"Resultado: {resultado:.2f} {para}", fg="green"
        )

    except ValueError:
        messagebox.showerror(
            "Erro", "Por favor, insira um número válido no valor!"
        )

janela = tk.Tk()
janela.title("SENAI - Sistemas")
janela.tk_setPalette(background="#dcdad5")

valor_label = tk.Label(janela, text="Valor da moeda:")
valor_label.grid(row=0, column=0, sticky="ns", padx=8, pady=8)

moeda_origem = tk.Label(janela, text="Moeda de Origem:")
moeda_origem.grid(row=1, column=0, sticky="ns", padx=8, pady=8)

moeda_destino = tk.Label(janela, text="Moeda de destino:")
moeda_destino.grid(row=2, column=0, sticky="ns", padx=8, pady=8)

entrada_valor = tk.Entry(janela, width=24, bg="lightgray")
entrada_valor.grid(row=0, column=1, sticky="ns", padx=8, pady=8)

combo_origem = ttk.Combobox(janela, values=["BRL", "USD", "EUR"], state="readonly", width=25)
combo_origem.grid(row=1, column=1, sticky="ns", padx=5, pady=5)
combo_origem.set("BRL")

combo_destino = ttk.Combobox(janela, values=["BRL", "USD", "EUR"], state="readonly", width=25)
combo_destino.grid(row=2, column=1, sticky="ns", padx=5, pady=5)
combo_destino.set("USD") 

button = tk.Button(
    janela,
    text="Converter",
    command=conversao_button,
    activebackground="blue",
    activeforeground="white",)
button.grid(row=3, column=1, sticky="sn", padx=5, pady=5)

resultado_label = tk.Label(
    janela, text="Resultado: ", font=("Arial", 11, "bold")
)
resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()