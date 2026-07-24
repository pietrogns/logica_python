#Bloquear redimensionamento: root.resizable(False, False)
#Permitir Apenas uma Direção: root.resizable(True, False)
# Tamanh Mínimo e Máximo: 
# root.minsize(x valor, x valor)
# root.maxsize(~ , ~)

import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

root.resizable(True, True)

root.minsize(300, 200)
root.maxsize(900, 900)

# comando de baixo serve para ajustar a transparência da janela
root.attributes("-alpha", 0.2)

root.mainloop()