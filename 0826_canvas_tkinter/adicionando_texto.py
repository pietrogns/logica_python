from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="gray")
#                               sintaxe
# canvas.create_text(x, y, text="seu texto", font=("Arial", 12), fill="cor")
canvas.create_text(200, 70, text="Pietro!", font=("Arial", 50, "bold"), anchor="nw", fill="cyan")
canvas.create_text(140, 50, text="pi", font=("Arial", 29, "bold"), anchor="e", fill="red")
canvas.create_text(120, 150, text="etro", font=("Arial", 40, "bold"), anchor="se", fill="purple")

#"bold" = adiciona negrito no texto
canvas.pack()
janela.mainloop()