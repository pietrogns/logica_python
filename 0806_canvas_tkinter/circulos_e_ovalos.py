from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="dark blue")
#Círculo
canvas.create_oval(
    50,50, 150, 150,
    fill="cyan"
)

#Óvalo
canvas.create_oval(
    200,200, 350, 250,
    fill="yellow"
)
canvas.pack()
janela.mainloop()
