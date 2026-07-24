tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro():
    print("\nTabuleiro:\n\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("_" *9)
        print()

def verificar_vitoria(jogador):
    #linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True
        
    #colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for lin in range(3)):
            return True
        
    #diagonais
    for c in range(2):
        if all(tabuleiro[linha][col] == jogador for linha, col in range(3)):
            return True
        
    
        
    return False


def jogar ():
    jogadas = 0
    jogador_atual = "X"

    while True: 
        mostrar_tabuleiro()
        print(f"Jogador {jogador_atual}")
        linha = int(input("escolha a linha da jogada entre 0 e 2: "))
        coluna = int(input("escolha a coluna da jogada entre 0 e 2: "))


        # Verifica se a posição esta livre
        if tabuleiro[linha][coluna] != " ":
            print("posição ocupada! Tente novamente.")
            continue

        #Faz a jogada
        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1 

        #Verificar vitória
    
        if verificar_vitoria(jogador_atual):
            mostrar_tabuleiro()
            print(f"O jogador {jogador_atual} venceu!")
            break


        #Verifica empate
        if jogadas == 9 :
            mostrar_tabuleiro()
            print("Houve empate!")
            break



        #Alterna jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"
        

jogar()

#if "all" = 