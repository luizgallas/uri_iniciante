sinal = input()
matriz = []

for i in range(12):
    for j in range(12):
        valor = float(input())
        if i < j:
            matriz.append(valor)

if sinal == "S":
    print(("%.1f")%(sum(matriz)))
elif sinal == "M":
    print(("%.1f")%(sum(matriz)/len(matriz)))