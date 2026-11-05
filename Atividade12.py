#Use um while para pedir ao usuário que digite "S" para continuar. O programa deve repetir a pergunta enquanto ele digitar qualquer outra  coisa.

while True:
    x = str(input("Digite S para sair:"))

    print(x)
    
    if x == 'S':
        break
