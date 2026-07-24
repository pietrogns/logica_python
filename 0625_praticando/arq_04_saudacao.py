def saudacao(nome = "Visitante"):
    """Função que recebe um nome e retorna uma saudação"""
    return f"Olá, {nome}!"

print(saudacao("Alice"))
print(saudacao())

#chamada sem argumento argumento = saudar() -> usa "Visitante", CHAMADA COM ARGUMENTO = saudar("Ana") -> usa "Ana"
#Sempre usar nomes descritivos