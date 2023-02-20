OUTCOMES = [
    "CX", "AY", "BZ",   #Vitória
    "AX", "BY", "CZ",   #Empate
    "BX", "CY", "AZ"    #Derrota
]

arquivo = open("input.txt", "r")

linha = arquivo.readline()

pts1 = 0
pts2 = 0

while linha.__len__() != 0:
    l = linha.split()

    # Parte 1
    jogada = l[0] + l[1]
    resultado = OUTCOMES.index(jogada)
    if resultado <= 2:
        pts1 += 6
    elif resultado <= 5:
        pts1 += 3
    pts1 += (resultado % 3) + 1

    # Parte 2


    linha = arquivo.readline()

print(pts1)