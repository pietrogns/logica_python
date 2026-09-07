import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")
janela.config()
janela.title("Calculadora de resistor")

CORES = {
    "Preto":    {"digito":0, "multi": 1, "cor":"#000000"},
    "Marrom":   {"digito":1, "multi":10, "cor":"#A52A2A"},
    "Vermelho": {"digito":2, "multi":100, "cor":"#FF0000"},
    "Laranja":  {"digito":3, "multi":1000, "cor":"#FF8C00"},
    "Amarelo":  {"digito":4, "multi":10000, "cor":"#FFA500"},
    "Verde":    {"digito":5, "multi":100000, "cor":"#008000"},    
    "Azul":     {"digito":6, "multi":1000000, "cor":"#0000FF" },
    "Violeta":  {"digito":7, "multi":10000000, "cor":"#8A2BE2"},
    "Cinza":    {"digito":8, "multi":None, "cor":"#808080"},
    "Branco":   {"digito":9, "multi":None, "cor":"#FFFFFF"},
    "Ouro":     {"digito":None,"multi":0.1,"cor":"#D4AF37" },
    "Prata":    {"digito":None,"multi":0.01,"cor":"#C0C0C0"}
}
TOLERANCIA = {
    "Marrom": ("#A52A2A", "±1%"),
    "Vermelho":("#FF0000","±2%"),
    "Ouro": ("#D4AF37","±5%"),
    "Prata": ("#C0C0C0","±10%")}

# cores que servem para as duas primeiras faixas (têm dígito 0-9)
NOMES_DIGITO = [nome for nome, info in CORES.items() if info["digito"] is not None]
# cores que servem para a faixa do multiplicador
NOMES_MULTI = [nome for nome, info in CORES.items() if info["multi"] is not None]
NOMES_TOLERANCIA = list(TOLERANCIA.keys())
 
# mapas inversos, usados no modo "por valor"
DIGITO_PARA_COR = {info["digito"]: nome for nome, info in CORES.items() if info["digito"] is not None}
MULTI_PARA_COR = {info["multi"]: nome for nome, info in CORES.items() if info["multi"] is not None}

UNIDADES = {"Ω": 1, "kΩ": 1_000, "MΩ":1_000_000}

def formatacao_valor(ohms):
    if ohms >= 1_000_000:
        return f"{ohms / 1_000_000:.2f} MΩ"
    elif ohms >= 1_000:
        return f"{ohms / 1_000:.2f} kΩ"
    else:
        return f"{ohms:.2f} Ω"

def modo_cores():
    print(f"opcao slecionada: {var_opcao.get()}")


# --- Interface ---
 
label_1 = tk.Label(janela, text="Calculadora de resistor", font=("Arial", 14, "bold"))
label_1.pack(anchor="w",pady=10)

#variavel para armazenar a opção selecionada
var_opcao = tk.StringVar(value="1")

frame_radios = tk.Frame(janela)
frame_radios.pack(anchor="w", padx=10, pady=5)

#columnspan=2 faz o texto ocupar o espaço de 2 colunas
escolha_modos = tk.Label(frame_radios, text="Como deseja informar o resistor?", font=("Arial", 10, "bold"))
escolha_modos.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))

rb1 = tk.Radiobutton(frame_radios, text="Cores", variable=var_opcao, value="1")
rb1.grid(row=1, column=0, sticky="w", padx=(0, 15))

rb2 = tk.Radiobutton(frame_radios, text="Valor", variable=var_opcao, value="2")
rb2.grid(row=1, column=1, sticky="w") # row 0, coluna 1
#       ^^^^^^^  ^^^^^^^^
#     mesma linha, coluna diferente = LADO A LADO


janela.mainloop()