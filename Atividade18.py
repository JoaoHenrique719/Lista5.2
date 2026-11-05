#Crie um loop while que permita ao jogador adicionar itens a uma lista de inventário até que ele digite "sair".


while True:
    lista = str(input("Digite os itens da sua lista, digite (Sair) para encerra a lista:"))

    if lista == "Sair":
        print("Saindo da lista de itens.")
        break
