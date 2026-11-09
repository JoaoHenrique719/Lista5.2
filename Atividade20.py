#Imagine uma corrida com 5 ciclistas (como no exercício de lógica do seu material). Use um loop para ler o tempo de cada um e identificar quem teve o menor tempo.
x = 1
tempo = 2
menor_tempo = 1
print(f"O {x}° ficou com o tempo de {menor_tempo} minutos.")
x += 1

for i in range(4):
    
    print(f"O {x}° ficou com o tempo de {tempo} minutos.")
    x += 1
    tempo += 2
    
print(f"O vencedor ficou com {menor_tempo} minutos!!")
