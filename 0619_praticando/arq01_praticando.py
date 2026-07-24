col = int(input("Digite o número de colunas: "))
lin = int(input("Digite o número de linhas: "))

print("+"+col*"-"+"+")

#comando para printar as linhas "+---+"

for i in range (lin):
    print("|"+" "*col+"|")

#comando para printar certa quantidade de colunas "|   |"

print("+"+col*"-"+"+")

#novamente comando para printar as linhas "+---+"

#forma do professor
# print("+", end="")
# for c in range(2,20):
#     print('-', end="")
# print('-')

# for l in range(2, 5):
#     print('|', end='')
#     for c in range(2,20):
#         print(' ', end="")
#     print('|')

# print("+", end="")
# for c in range(2,20):
#     print('-', end="")
# print('-')