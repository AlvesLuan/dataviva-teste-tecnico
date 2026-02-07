def e_palindromo(palavra):
    #coloco a palavra enviada em minusculo pra evitar erro, apenas.
    palavra = palavra.lower()

    #apenas comparo com a palavra inversa usando slicing
    if palavra == palavra[::-1]: 
        return True
    else:
        return False 

a_ser_validado = str(input("digite sua palabra: "))
resultado = e_palindromo(a_ser_validado)  
print(resultado)
