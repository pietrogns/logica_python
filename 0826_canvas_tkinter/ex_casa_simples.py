from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("800x600")

canvas = Canvas(janela, width=700, height=500, bg="aqua")



# canvas.create_line(
#    110, 110, 150, 110,
#    fill="blue",
#    width=3)

# #linha reta para baixo
# canvas.create_line(
#    200, 200, 110, 200,
#    fill="orange",
#    width=3)

# #linha reta para baixo
# canvas.create_line(
#    200, 200, 200, 110,
#    fill="purple",
#    width=3)

#Base da casa
canvas.create_rectangle(
    300,250, 150, 150,
    fill="white"
)

#Triângulo
canvas.create_polygon(220,30,
                      300,150
                      ,150,150,
                      fill="brown")

#Janela esquerda

#linha para baixo dir
canvas.create_line(
   190, 210, 190, 180,
   fill="brown",
   width=3)

#linha para baixo esq
canvas.create_line(
   160, 210, 160, 180,
   fill="brown",
   width=3)

#linha reta baixo
canvas.create_line(
   159, 210, 192, 210,
   fill="brown",
   width=3)

#linha reta de cima
canvas.create_line(
   159, 180, 192, 180,
   fill="brown",
   width=3)

#linha do meio para baixo
canvas.create_line(
   175, 210, 175, 180,
   fill="gray",
   width=3)

#linha reta do meio
canvas.create_line(
   159, 195, 190, 195,
   fill="gray",
   width=3)

#Janela direita

#linha para baixo dir
canvas.create_line(
   290, 210, 290, 180,
   fill="brown",
   width=3)
#linha para baixo esq
canvas.create_line(
   260, 210, 260, 180,
   fill="brown",
   width=3)

#linha reta de baixo
canvas.create_line(
   259, 210, 292, 210,
   fill="brown",
   width=3)

#linha reta de cima
canvas.create_line(
   259, 180, 292, 180,
   fill="brown",
   width=3)

#linha do meio para baixo
canvas.create_line(
   275, 210, 275, 180,
   fill="gray",
   width=3)

#linha reta do meio
canvas.create_line(
   259, 195, 292, 195,
   fill="gray",
   width=3)


#Porta
canvas.create_rectangle(
    200, 250, 250, 190,
    fill="light gray"
)

#Maçaneta
canvas.create_oval(
    202,220, 210, 215,
    fill="black"
)

#Grama
canvas.create_rectangle(
    800,600, 1, 250,
    fill="green"
)

canvas.pack()
janela.mainloop()
