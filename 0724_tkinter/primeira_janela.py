import tkinter as tk

# Cria a janela principal
root = tk.Tk()
root.title("Desenvolvimento de Sistemas - SENAI")

# Esse comando serve para ler o título da janela
tittle = root.title()

# Cria um rótulo (label) com o texto "Olá, mundo!"
message = tk.Label(root, text = "Olá, mundo!")
message1 = tk.Label(root, text = "mundo!")

# Posiciona o rótulo na janela
message.pack()
message1.pack()

# Para aumentar o tamanho usa o comando:
root.geometry("600x400+50+50")
#600 = largura
#400 = Altura
#+50+50 = Posição X e Y

# Inicia o loop principal da interface gráfica
root.mainloop()