print("Digite nomes (pressione Enter em branco para terminar): ")
nomes = []
while True:
    nome = input("digite o nome: " ).strip()
    if nome == "":
        break
    nomes.append(nome)

with open("nomes.txt", "w+", encoding="utf-8") as f:
    for n in nomes:
        f.write(n + "\n")

#vamos nessa!
#with open("nomes.txt", "r", enconding="utf-8") as f:
# conteudo = f.read()
#print(conteudo)