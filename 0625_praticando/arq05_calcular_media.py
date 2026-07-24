def calcular_media (numeros):
    """
    recebe uma lista de inteiros e retorna a media aritmetica.
    
    parametros:
    - numeros: lista de inteiros
    
    Retorna:
    - float: media aritmetica(0.0 se a lista for vazia)
    """

    if not numeros:
        return 0.0
    total = sum(numeros)
    return float(total) / len(numeros)

exemplo = [7, 8 , 9, 10]
resultado = calcular_media(exemplo)
print(resultado)