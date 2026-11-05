#Em um motor de jogo, queremos criar 100 partículas de fogo. Escreva a estrutura de um loop que repetirai a função criar_particulas() 100 vezes.
x = 1

for i in range(100):
    print(f"{x} fagulhas criadas.")
    x += 1
