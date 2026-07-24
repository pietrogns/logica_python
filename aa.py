with open('arq_filmes.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()
    
    # Exibe a 5ª linha (índice 4)
    print(linhas[2].strip())

