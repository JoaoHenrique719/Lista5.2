#Um herói ataca um mostro 5 vezes. a cada ataque, o monstro perde 10 de vida. Se a vida_mostro começa em 50, use um loop para mostrar a vida diminuindo a cada golpe.

vida_monstro = 50
for i in range(5):
    vida_monstro -= 10
    print(f" O herói atacou, e o monstro está com {vida_monstro} de vida.")
