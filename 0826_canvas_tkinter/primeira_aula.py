#para importar: "From tkinter import Tk, Canvas"
#Criar janela: janela = Tk()
#Criar Canvas: canvas =Canvas(janela, width=400, height=300, bg="yellow")
#exibir: canvas.pack()
#Janela.mainloop()


#MODELO INICIAL
from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="yellow")

#codigo vai abaixo 


canvas.pack()
janela.mainloop()