def encontrar_duplicado(lista):
    #coloca o conjunto de numeros em uma hashSet
    numeros = set()
    
    #busca no hashset
    for numero_atual in lista:
        if numero_atual in numeros:
            return numero_atual
        numeros.add(numero_atual)
    
    return "não há repetidos"  

verificação = encontrar_duplicado([1, 2, 3, 4, 5, 6])
print(verificação) 
