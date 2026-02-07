def somar_categorias(lista_dicio):
    #criei um dicionario vazio que vai ser alimentado com a categoria e ao lado sua soma total
    totais_por_categoria = {}

    for elemento in lista_dicio:
        #só extraio as info de cada dicionário da lista que foi passada
        categoria = elemento["categoria"]
        valor = elemento["valor"]

        if categoria in totais_por_categoria:
            totais_por_categoria[categoria] += valor
        else: #primeira aparicao de cada categoria vai levar direto pro dicionario de result já q ela n existe, se ja existir entra no if de cima e só pega o valor e soma.
            totais_por_categoria[categoria] = valor

    return totais_por_categoria


resultado = somar_categorias([
    {"categoria": "Alimentação", "valor": 10},
    {"categoria": "Transporte", "valor": 5},
    {"categoria": "Alimentação", "valor": 20},
    {"categoria": "Lazer", "valor": 50}
])

#resultado cru é {'Alimentação': 30, 'Transporte': 5, 'Lazer': 50}
print("{")
for categoria, valor in resultado.items():
    print(f"'{categoria}': {valor},")
print("}")
