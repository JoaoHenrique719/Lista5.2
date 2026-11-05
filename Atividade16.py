#Simule uma barra de caregamendo que imprima "Carregando...10%", "Carregando...20%" Até 100%, aumentando de 10 em 10.

x = 10
for i in range (10):
    print(f"Carregando {x}%")
    x += 10
