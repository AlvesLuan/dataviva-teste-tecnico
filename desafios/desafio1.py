for i in range(1, 101):
    texto = ""
    if i % 3 == 0:
        texto += "Fizz"
    if i % 5 == 0:
        texto += "Buzz"
    print(texto if texto else i) #só printa Fizz, Buzz ou FizzBuzz se a condicional alimentar a variavel texto
