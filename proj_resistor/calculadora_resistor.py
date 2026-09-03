from tkinter import Tk, Canvas
from tkinter import ttk
import tkinter as tk

janela = Tk()
janela.geometry("500x400")
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

NOMES_CORES = list(CORES.keys())
NOMES_TOLERANCIA = list(TOLERANCIA.keys())

def formatacao_valor(ohms):
    if ohms >= 1_000_000:
        return f"{ohms / 1_000_000:.2f} MΩ"
    elif ohms >= 1_000:
        return f"{ohms / 1_000:.2f} kΩ"
    else:
        return f"{ohms:.2f} Ω"

#título do tkinter
label_1 = tk.Label(janela, text="Calculadora de resistor", anchor= "n")
label_1.pack()
janela.mainloop()

#canvas onde o resistor vai ser desenhado
canvas = tk.Canvas(janela, width=350, height=200, bg="gray")
canvas.pack(pady=20)
