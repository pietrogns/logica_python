from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="gray")

#Triângulo
canvas.create_polygon(100,50,
                      150,150
                      ,50,150,
                      fill="green")

canvas.pack()
janela.mainloop()

#sintaxe
# canvas.create_polygon(x1,y1,
#                       x2,y2
#                       ,x3,y3,...,
#                       fill="cor")