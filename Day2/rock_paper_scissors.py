OUTCOMES1 = [
    "CX", "AY", "BZ",   #Vitória
    "AX", "BY", "CZ",   #Empate
    "BX", "CY", "AZ"    #Derrota
]

OUTCOMES2 = [
    "CZ", "AZ", "BZ",   #Vitória
    "AY", "BY", "CY",   #Empate
    "BX", "CX", "AX"    #Derrota
]

arquivo = open("input.txt", "r")

linha = arquivo.readline()

pts1 = 0
pts2 = 0

while linha.__len__() != 0:
    l = linha.split()
    jogada = l[0] + l[1]

    # Parte 1
    resultado = OUTCOMES1.index(jogada)
    if resultado <= 2:
        pts1 += 6
    elif resultado <= 5:
        pts1 += 3
    pts1 += (resultado % 3) + 1

    # Parte 2
    resultado = OUTCOMES2.index(jogada)
    if resultado <= 2:
        pts2 += 6
    elif resultado <= 5:
        pts2 += 3
    pts2 += (resultado % 3) + 1

    linha = arquivo.readline()

print(pts1)
print(pts2)