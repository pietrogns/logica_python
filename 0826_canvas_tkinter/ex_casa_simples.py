from tkinter import Tk, Canvas
janela = Tk()
janela.geometry("800x600")

canvas = Canvas(janela, width=700, height=500, bg="aqua")
#Base da casa
canvas.create_rectangle(300,250, 150, 150,fill="white")
#Triângulo
canvas.create_polygon(220,40,300,150,150,150,fill="brown")

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
canvas.create_line(290, 210, 290, 180,fill="brown",width=3)
#linha para baixo esq
canvas.create_line(260, 210, 260, 180,fill="brown",width=3)
#linha reta de baixo
canvas.create_line(259, 210, 292, 210,fill="brown",width=3)
#linha reta de cima
canvas.create_line(259, 180, 292, 180,fill="brown",width=3)
#linha do meio para baixo
canvas.create_line(275, 210, 275, 180,fill="gray",width=3)
#linha reta do meio
canvas.create_line(259, 195, 292, 195,fill="gray",width=3)

#Porta
canvas.create_rectangle(200, 250, 250, 190,fill="light gray")
#Maçaneta
canvas.create_oval(202,220, 210, 215,fill="black")
#Grama
canvas.create_rectangle(800,600, 1, 250,fill="green")

# Carro (Traseira e teto)
canvas.create_polygon(430, 150, 495, 150, 515, 170, 515, 190, 430, 190, fill="red", outline="black")

# Frente carro
canvas.create_polygon(430, 165, 430, 190, 410, 190, 410, 175, fill="red", outline="black")

# Porta carro
canvas.create_rectangle(435, 168, 468, 188, fill="red", outline="black")

# Maçaneta porta 
canvas.create_oval(460, 174, 466, 177, fill="silver", outline="black")

# Vidro dianteiro
canvas.create_polygon(417, 168, 431, 155, 431, 168, fill="cyan", outline="black")

# Janela da Porta
canvas.create_rectangle(435, 155, 468, 168, fill="cyan", outline="black")

# Janela Traseira
canvas.create_polygon(472, 155, 495, 155, 505, 168, 472, 168, fill="cyan", outline="black")

# Roda Esquerda
canvas.create_oval(423, 182, 443, 202, fill="black", outline="")
canvas.create_oval(431, 190, 435, 194, fill="white", outline="")

# Roda Direita
canvas.create_oval(487, 182, 507, 202, fill="black", outline="")
canvas.create_oval(495, 190, 499, 194, fill="white", outline="")

# Farol dianteiro
canvas.create_rectangle(410, 176, 413, 182, fill="yellow", outline="")
canvas.pack()
janela.mainloop()