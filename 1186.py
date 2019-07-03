operacao = input()
matriz = []

for i in range(12):
    for j in range(12):
        valor = float(input())
        if (i + j > 11):
            matriz.append(valor)

if operacao == "S":
    print(("%.1f")%(sum(matriz)))
elif operacao == "M":
    print(("%.1f")%(sum(matriz)/len(matriz)))