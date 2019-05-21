col = int(input())
op = input()
soma = 0

mat = [[0.0]*12 for i in range(12)]

for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())
        if j == col:
            soma += mat[i][j]

if op == "S":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/12))

