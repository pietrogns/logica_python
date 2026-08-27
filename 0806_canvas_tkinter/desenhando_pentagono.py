from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="gray")

canvas.create_polygon(110,100,
                      60,100
                      ,100,60,
                      150,110,
                      fill="cyan")

#sintaxe
# canvas.create_polygon(x1,y1,
#                       x2,y2
#                       ,x3,y3,...,
#                       fill="cor")
canvas.pack()
janela.mainloop()