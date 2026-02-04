def e_palindromo(palavra):
    #apenas comparo com a palavra inversa
    if palavra == palavra[::-1]:
        return "é palindromo!"
    else:
        return "não é palindromo!" 

a_ser_validado = str(input("digite sua palabra: "))
resultado = e_palindromo(a_ser_validado)  
print(resultado)
