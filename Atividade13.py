#Escreva um código que percorra o itnervalo de 1 a 20 e imprima apenas os números que são pares.

x = 1
while x < 21:
    x += 1
    y = x % 2
    
    if y == 0:
        print(x)
