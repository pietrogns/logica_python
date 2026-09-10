import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas
from tkinter import messagebox
janela = Tk()
janela.geometry("500x400")
janela.config(background="light gray")
janela.title("Calculadora de resistor")

estilo = ttk.Style()
estilo.theme_use('clam')
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
    opcao = modo_var.get()
    
    if opcao == "cores":
        # Se você já tiver criado o frame_valor_cor, esconda-o aqui:
        frame_valor_cor.pack_forget()
        
        # Mostra o frame_cor_valor exatamente DEPOIS do frame_modo
        frame_cor_valor.pack(after=frame_modo, pady=10)
        
    elif opcao == "valor":
        # Esconde o frame de cores
        frame_cor_valor.pack_forget()
        
        # Mostra o frame_valor_cor exatamente DEPOIS do frame_modo
        frame_valor_cor.pack(after=frame_modo, pady=10)

def botao_calcular():
        messagebox.showinfo(
        "Informação",
        "Você clicou no botão!"
    )
#  Interface 
label_titulo = tk.Label(janela, text="Calculadora de resistor", anchor= "n", bg="light gray", font=("Arial", 16, "bold"))
label_titulo.pack()

# opções de modos
frame_modo = tk.Frame(janela, bg="light gray")
frame_modo.pack(fill="x", pady=5)
modo_var = tk.StringVar(value="cores") 

#botões das opções
cores_rdbtn = tk.Radiobutton(frame_modo, text="Cores do resistor", variable=modo_var, value="cores", bg="Gainsboro", font=("Arial", 9),command=modo_cores).pack(side="left", padx=5)
valor_rdbtn = tk.Radiobutton(frame_modo, text="Valor do resistor", variable=modo_var, value="valor", bg="Gainsboro", font=("Arial", 9),command=modo_cores).pack(side="left", padx=5)

#--------- Comboboxes para seleção de cores ---------
frame_cor_valor = tk.LabelFrame(janela, padx=10, pady=10)
frame_cor_valor.pack(pady=10)

faixa1_txt = tk.Label(frame_cor_valor, text="Faixa 1")
faixa1_txt.grid(row=0, column=0, padx=5)
faixa1_combo = ttk.Combobox(frame_cor_valor, values=NOMES_DIGITO, state="readonly", width=13)
faixa1_combo.grid(row=1, column=0, padx=5, pady=5)

faixa2_txt = tk.Label(frame_cor_valor, text="Faixa 2")
faixa2_txt.grid(row=0, column=1, padx=5)
faixa2_combo = ttk.Combobox(frame_cor_valor, values=NOMES_DIGITO, state="readonly", width=13)
faixa2_combo.grid(row=1, column=1, padx=5, pady=5)

#faixa multiplicador
faixa3_txt = tk.Label(frame_cor_valor, text="Multiplicador:")
faixa3_txt.grid(row=0, column=2, padx=5)
faixa3_combo = ttk.Combobox(frame_cor_valor, values=NOMES_MULTI, state="readonly", width=13)
faixa3_combo.grid(row=1, column=2, padx=5, pady=5)

#faixa tolerância
faixa4_txt = tk.Label(frame_cor_valor, text="Tolerância:")
faixa4_txt.grid(row=0, column=3, padx=5)
faixa4_combo = ttk.Combobox(frame_cor_valor, values=NOMES_TOLERANCIA, state="readonly", width=13)
faixa4_combo.grid(row=1, column=3, padx=5, pady=5)

#--------- Valor Resistência ---------

frame_valor_cor = tk.LabelFrame(janela,padx=10, pady=10)

#texto que mostra onde o usuario vai digitar 
resis_valor = tk.Label(frame_valor_cor, text="Valor da Resistência (Ω)")
resis_valor.grid(row=0, column=0, padx=5)
entry_resis = tk.Entry(frame_valor_cor)
entry_resis.grid(row=1, column=0, padx=5, pady=5)

toler_combo = ttk.Combobox(frame_valor_cor, values=NOMES_TOLERANCIA,state="readonly", width=13)
toler_combo.grid(row=1, column=1, padx=5, pady=5)


#canvas onde o resistor vai ser desenhado
resist_canvas = tk.Canvas(janela, width=400, height=200)
resist_canvas.pack()

botton_calcular = tk.Button(janela, text="Calcular resistência", fg="light green",command=botao_calcular)
janela.mainloop()