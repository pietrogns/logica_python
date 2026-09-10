#Exemplo visual na prática
#Imagine que você quer criar um formulário com o título no topo e duas colunas de botões abaixo:

import tkinter as tk

janela = tk.Tk()
janela.geometry("300x150")

# 1. Título direto na janela principal usando PACK
titulo = tk.Label(janela, text="Selecione o Modo:", font=("Arial", 12, "bold"))
titulo.pack(pady=10)

# 2. Criamos um FRAME para segurar os RadioButtons
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)  # Colocamos o Frame na janela com PACK

var_modo = tk.StringVar(value="Cores")

# 3. Agora usamos GRID DENTRO do frame_botoes para colocar lado a lado
rb1 = tk.Radiobutton(frame_botoes, text="Por Cores", variable=var_modo, value="Cores")
rb1.grid(row=0, column=0, padx=10)

rb2 = tk.Radiobutton(frame_botoes, text="Por Valor", variable=var_modo, value="Valor")
rb2.grid(row=0, column=1, padx=10)

janela.mainloop()