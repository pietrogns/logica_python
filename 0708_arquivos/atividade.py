nomes  = []
for i in range(3):
    nom = input("Insira seu nome: ")
    nomes.append(nom)
with open("nomes.txt", "w", encoding="utf-8") as f:
    for nome in nomes:
        f.write(nome + "\n")