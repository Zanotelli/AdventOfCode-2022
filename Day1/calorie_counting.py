arquivo = open("input.txt", "r")

dic = []
dic.append([])

linha = arquivo.readline()
i = 0

## Part 1
elfTop = [0, 0]
elfTopThree = [0, 0, 0]
while linha.__len__() != 0:
    if linha != '\n':
        dic[i].append(int(linha.split()[0]))
    else:
        soma = sum(dic[i])
        if soma > sum(dic[elfTop[0]]):
            elfTop[0] = i
            elfTop[1] = soma
        if soma > elfTopThree[0] or soma > elfTopThree[1] or soma > elfTopThree[2]:
            elfTopThree[elfTopThree.index(min(elfTopThree))] = soma
        dic.append([])
        i += 1

    linha = arquivo.readline()

print("[Elf number, Calories] -> ", elfTop)
print("Total snaks from top 3 -> ", sum(elfTopThree))

## Part 2

