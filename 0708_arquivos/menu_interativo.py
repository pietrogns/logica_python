def menu():
    print("\nMenu:")
    print("0 - Adicionar filme (opcional)")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")

def adicionar_filme():
    print("Informe os dados do filme:")
    titulo = input("Título: ").strip()
    ano = input("Ano: ").strip()
    diretor = input("Diretor: ").strip()
    genero = input("Gênero: ").strip()
    duracao = input("Duração: (ex: 120 minutos): ").strip()

    with open("arq_filme.txt", "a", encoding= "utf-8") as f:
        f.write("\n")
        f.write(f"Título: {titulo}\n")
        f.write(f"Ano: {ano}\n")
        f.write(f"Diretor: {diretor}\n")
        f.write(f"Gênero: {genero}\n")
        f.write(f"Duração: {duracao}\n")

    print("Filme adicionado com sucesso")


    #COMANDO QUE FIZEMOS
    # print("Adicionar filme")
    # ins_titulo = input("Digite o título do filme: ")
    # ins_ano = int(input("Digite o ano em que foi lançado o filme: "))
    # ins_diretor = input("Digite o nome do diretor do filme: ")
    # ins_genero = input("Digite o gênero do filme: ")
    # ins_duracao = input("Digite quantos minutos de duração tem no filme: ").strip()

    # total_filmes = 0

    # with open('arq_filme.txt', 'a', encoding='utf-8') as f:
    #     for linha in f:
    #         linha_limpa = linha.strip()
    #         if "Título" in linha_limpa:
    #             total_filmes += 1 

    # print(f"{total_filmes}")

def contar_filmes():

    print("Contar filmes\n")

    total_filmes = 0 
    
    with open('arq_filme.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            linha_limpa = linha.strip()
            
            print(linha_limpa)
            
            if "Título" in linha_limpa:
                total_filmes += 1 
                
    print(f"\nTotal de filmes encontrados: {total_filmes}")


def info_por_titulo():
    titulo_busca = input("Digite o título do filme: ").strip().lower()
    encontrado = False
    try:
        with open('arq_filme.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                if linha.strip().startswith("Título:"):
                    titulo = linha.split(":", 1)[1].strip()
                    if titulo.lower() == titulo_busca:
                        print(f"Título: {titulo}")
                        try:
                            ano = next(f).strip()
                            diretor = next(f).strip()
                            genero =  next(f).strip()
                            duracao =  next(f).strip()
                        except StopIteration:
                            print("Registro incompleto para esse título.")
                            return
    
                        print(ano)
                        print(diretor)
                        print(genero)
                        print(duracao)
                        encontrado = True
                        break

    except FileNotFoundError:
        print("Arquivo 'arq_filme.txt' não encontrado")
        return
    if not encontrado:
        print("Filme não encontrado!")

def filmes_por_diretor():
    print("Filmes por diretor")
    diretor_busca = input("Diretor: ").strip().lower()
    contador = 0
    try:
        with open("arq_filme.txt", encoding="utf-8") as f:
            ultim_titulo = ""
            for linha in f:
                s = linha.strip()
                if s.startswith("Título:"):
                    ultimo_titulo = s.split(":", 1) [1].strip()
                elif s.startswith("Diretor:"):
                    diretor = s.split(":", 1) [1].strip()
                    if diretor.lower() == diretor_busca:
                        contador += 1
                        print(f"- {ultimo_titulo}")
    except FileNotFoundError:
        print("Arquivo 'arq_filme.txt' não encontrado.")
        return

    print(f"Total de filmes do diretor '{diretor_busca}': {contador}")
    return contador

def filmes_por_genero():
    print("Filmes por genero")
    genero_busca = input("Gênero: ").strip().lower()
    contador = 0
    try:
        with open("arq_filme.txt", encoding="utf-8") as f:
            ultimo_titulo = ""
            for linha in f:
                s = linha.strip()
                if s.startswith("Título:"):
                    ultimo_titulo = s.split(":", 1) [1].strip()
                elif s.startswith("Gênero:"):
                    genero = s.split(":", 1) [1].strip()
                    if genero_busca in genero.lower():
                        contador += 1
                        print(f"- {ultimo_titulo} ({genero})")
    except FileNotFoundError:
        print("Arquivo 'arq_filme.txt' não encontrado.")
        return
    print(f"Total de filmes do gênero '{genero_busca}': {contador}")
    return contador

def media_duracao():
    print("Média da duração")
    soma = 0
    cont = 0
    try:
        with open("arq_filme.txt", encoding ="utf-8") as f:
            for linha in f:
                s = linha.strip()
                if s.startswith("Duração:"):
                    try:
                        minutos = int(s.split(":", 1) [1].strip().split()[0])
                    except (ValueError, IndexError):
                        #IGNORA VALORES INVÁLIDOS
                        continue
                    soma += minutos
                    cont += 1
    except FileNotFoundError:
        print("Arquivo 'arq_filme.txt' não encontrado.")
        return

    if cont == 0:
        print("Nenhuma duração válida encontrada.")
    else:
        media = soma / cont
        print(f"Média de duração: {media:.2f} minutos")
        return media
    
while True:
    menu()
    opc = input("Escolha uma opção: ").strip()
    if opc == "0":
        adicionar_filme()         
    elif opc == "1":
        contar_filmes()
    elif opc == "2":
        info_por_titulo()
    elif opc == "3":
        filmes_por_diretor()
    elif opc == "4":
        filmes_por_genero()
    elif opc == "5":
        media_duracao()
    elif opc == "6":
        print("Saindo . . .")
        break
    else:
        print("Opção invalida. Tente novamente.")