def validacao_de_parenteses(conjunto):
    
    #De cara, se não for par alguma coisa ta errada
    if (len(conjunto) % 2 != 0):
        print("❌ Inválido")
        return

    else:
        
        pilha = []

        # dicionario relação chave -> valor
        pares = {
            ')': '(',
            ']': '[',
            '}': '{'
        } 

        for simboloAtual in conjunto:
            if simboloAtual in '([{':
                pilha.append(simboloAtual)

            elif simboloAtual in ')]}':
                #verifica se a pilha ta vazia ou se o topo da pilha é igual ao seu par
                if not pilha or pilha.pop() != pares[simboloAtual]:
                    print("❌ Inválido (ordem errada)")
                    return

        #sobrou na pilha, ent tá errado
        if pilha:
            print("❌ Inválido (falta fechar)")
        else:
            print("✅ Válido")
        
            


a_ser_validado = str(input("Validação de Parênteses\nDigite sua string: "))
validacao_de_parenteses(a_ser_validado)
