from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="dark blue")

canvas.create_rectangle(
    50,50, 150, 100,
    fill="cyan"
)


canvas.pack()
janela.mainloop()

#                 Sintaxe

# canvas.create_rectangle(x1,y1, x2, y2,
#                         fill="cor",
#                         outline="cor")

#(x1,y1) = canto superior esquerdo
#(x2, y2) = canto inferior direito

#(50,50) = canto superior esquerdo do retângulo
#(150, 100) = canto inferior direito do retângulo

#Eixo X: crescente para a direita
#Eixo Y: crescente para baixo