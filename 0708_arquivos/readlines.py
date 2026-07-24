with open("exemplo.txt", "r") as f:
    linhas = f.readlines()
    for linha in linhas:
        print(linha.strip())

# with open("exemplo.txt") as f:
#     for linha in f:
#         print(linha)

# esse método lê linha a linha automaticamente, sem precisar de readline()