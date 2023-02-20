arquivo = open("input.txt", "r")

dic = []
dic.append([])

linha = arquivo.readline()
i = 0

elf = [0, 0]

while linha.__len__() != 0:
    if linha != '\n':
        dic[i].append(int(linha.split()[0]))
    else:
        if sum(dic[i]) > sum(dic[elf[0]]):
            elf[0] = i
            elf[1] = sum(dic[i])
        print("Elfo", i," -> ", sum(dic[i]))
        dic.append([])
        i += 1

    linha = arquivo.readline()

print("Elfo mais gordo: ", elf)