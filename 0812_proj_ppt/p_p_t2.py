from tkinter import *
from tkinter import ttk
import random

# pip install Pillow

from PIL import Image, ImageTk

#cores ----------------------------------------
cor0 = "#FFFFFF" #white/ branca
cor1 = "#333333" #black/ preta
cor2 = "#fcc058" #orange/ laranja
cor3 = "#fff873" #yellow/ amarela
cor4 = "#34eb3d" #green/ verde
cor5 = "#e85151" #red / vermelha
fundo = "#3b3b3b"

janela = Tk()
janela.title("Pedra, Papel e Tesoura")
janela.geometry("260x285")
janela.configure(bg=fundo)




frame_cima = Frame(janela, width=260, height=100, bg=cor1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=300, bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

#configurando os jogadores

#jogador pessoa =  A
app_pessoa = Label(frame_cima, text="Jogador", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pessoa.place(x=10, y=70)

#barra marcou pontos = B
app_pessoa_linha = Label(frame_cima, text="", height=10, anchor="center", bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pessoa_linha.place(x=0, y=0)

#pontuação = C
app_pessoa_pontos = Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pessoa_pontos.place(x=50, y=20)

#separação da pontuação = D
app_vs = Label(frame_cima, text=":", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_vs.place(x=125, y=20)

#----------------------------------------------------------------------------------------------------------


#jogador pc

app_pc = Label(frame_cima, text="PC", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pc.place(x=220, y=70)

#barra marcou pontos
app_pc_linha = Label(frame_cima, text="", height=10, anchor="center", bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pc_linha.place(x=255, y=0)

#pontuação
app_pc_pontos = Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pc_pontos.place(x=180, y=20)

#barra empate
empate = Label(frame_cima, text="",width=260, anchor="center",bg=cor3, fg=cor0)
empate.place(x=0, y=95)

#mostra a jogada do pc
app_jogada_pc = Label(frame_baixo, text="", height=1, anchor="center",
                      bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pc.place(x=190, y=10)

#mostra a jogada do jogador
app_jogada_pessoa = Label(frame_baixo, text="", height=1, anchor="center",
                          bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pessoa.place(x=10, y=10)

global escolha_pessoa
global escolha_pc
global pontos_pessoa
global pontos_pc
global rodadas
pontos_pessoa = 0
pontos_pc = 0
rodadas = 5

    #setando a cor da marcação de ponto para ficarem invisiveis
app_pessoa_linha["bg"] = cor0
app_pc_linha["bg"] = cor0
empate["bg"] = cor0
#função terminar jogo
def terminar_jogo():
    pass

#função logica do jogo
def jogar(jogada):
    global pontos_pessoa
    global pontos_pc
    global rodadas
    opcoes = ["pedra", "papel", "tesoura"]



    if rodadas > 0:
        print(rodadas)
        #random serve para randomizar as opções do PC
        escolha_pc = random.choice(opcoes)
        app_jogada_pc["text"] = escolha_pc

        escolha_pessoa = jogada
        app_jogada_pessoa["text"] = escolha_pessoa
        print(escolha_pessoa, escolha_pc)
        rodadas -= 1

    # caso empate
        
    if escolha_pessoa == escolha_pc:
        empate["bg"] = cor3

    # elif testa_vitoria_pessoa(escolha_pessoa, escolha_pc):
    #     pontos_pessoa += 10
    #     app_pessoa_linha["bg"] = cor4
    # elif testa_vitoria_pc(escolha_pessoa, escolha_pc):
    #     pontos_pc += 10
    #     app_pc_linha["bg"] = cor4

    #  mostrar_pontos(ponto_pessoa, pontos_pc)
    else:
        terminar_jogo()

#função iniciar o jogo
def button_jogar():
    global icone_pedra
    global icone_papel
    global icone_tesoura
    global btn_pedra
    global btn_papel
    global btn_tesoura

    icone_pedra = Image.open("0812_proj_ppt/pedra.png")
    icone_pedra = icone_pedra.resize((50,50), Image.Resampling.LANCZOS)
    icone_pedra = ImageTk.PhotoImage(icone_pedra)
    btn_pedra = Button(frame_baixo, command=lambda:jogar("pedra"), width=50, height=50, image=icone_pedra,
                 compound="center", font=("Ivy 10 bold"),
                   anchor="center", relief="flat")
    btn_pedra.place(x=15, y=60)

    icone_tesoura = Image.open("0812_proj_ppt/tesoura.png")
    icone_tesoura = icone_tesoura.resize((50,50), Image.Resampling.LANCZOS)
    icone_tesoura = ImageTk.PhotoImage(icone_tesoura)
    btn_tesoura = Button(frame_baixo, command=lambda:jogar("tesoura"), width=50, height=50, image=icone_tesoura,
                 compound="center", font=("Ivy 10 bold"),
                   anchor="center", relief="flat")
    btn_tesoura.place(x=190, y=60)

    icone_papel = Image.open("0812_proj_ppt/papel.png")
    icone_papel = icone_papel.resize((50,50), Image.Resampling.LANCZOS)
    icone_papel = ImageTk.PhotoImage(icone_papel)
    btn_papel = Button(frame_baixo, command=lambda:jogar("papel"), width=50, height=50, image=icone_papel,
                 compound="center", font=("Ivy 10 bold"),
                   anchor="center", relief="flat")
    btn_papel.place(x=105, y=60)


#botão jogar
btn_jogar = Button(frame_baixo, command=button_jogar, text="Jogar", width=29, anchor="center",fg=cor0, bg=fundo, font=("Ivy 10 bold"))
btn_jogar.place(x=9, y=155)


janela.mainloop()

