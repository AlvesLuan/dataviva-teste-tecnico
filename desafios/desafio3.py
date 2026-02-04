def duplicados(lista):
    #cria 2 hashsets, uma pra todos os numeros e outra apenas pra duplicados
    numeros = set()
    duplicados = set()  

    #comparo o elemento atual com a set de numeros que esta sendo alimntada por esse for
    for num_atual in lista:
        if num_atual in numeros:
            duplicados.add(num_atual)
        else:
            numeros.add(num_atual)

    return list(duplicados)

print(duplicados([1, 2, 3, 2, 5]))
