GROUP_SIZE = 3

arquivo = open("input.txt", "r")
linha = arquivo.readline()

sum = 0
sum_badge = 0
group = list()
while linha.__len__() != 0:
    l = linha.split()[0]

    # Parte 1
    repeat = list(set(l[int(len(l)/2):]).intersection(l[:int(len(l)/2)]))[0]
    sum += (ord(repeat) - 96) if ord(repeat) - 96 > 0 else ord(repeat) - 38

    # Parte 2
    group = group + [l] if group.__len__() < GROUP_SIZE else list([l])
    badge = list(set.intersection(*map(set, group)))[0] if group.__len__() == GROUP_SIZE else ""
    sum_badge += (ord(badge) - 96 if ord(badge) - 96 > 0 else ord(badge) - 38) if badge != "" else 0

    linha = arquivo.readline()

print(sum)
print(sum_badge)

