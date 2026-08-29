#Sintaxe 
#canvas.create_line(
#   x1, y1, x2, y2,
#   fill="cor",
#   width=espessura)

from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="gray")

#linha diagonal
canvas.create_line(
   10, 10, 200, 200,
   fill="cyan",
   width=3)

#linha reta para baixo
canvas.create_line(
   10, 10, 10, 200,
   fill="red",
   width=3)

#linha reta 
canvas.create_line(
   10, 10, 200, 10,
   fill="blue",
   width=3)

#linha reta para baixo
canvas.create_line(
   200, 200, 10, 200,
   fill="orange",
   width=3)

#linha reta para baixo
canvas.create_line(
   200, 200, 200, 10,
   fill="purple",
   width=3)

canvas.pack()
janela.mainloop()
