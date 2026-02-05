def Validacao_de_Parenteses(conjunto):
    vetor = list(conjunto)

    #De cara, se não for par alguma coisa ta errada
    if (len(vetor) % 2 != 0):
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

        for simboloAtual in vetor:
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
Validacao_de_Parenteses(a_ser_validado)
