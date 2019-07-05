sinal = input()
soma = 0
acc = 0

for i in range(12):
  for j in range(12):
    matriz = float(input())
    if(i + j >= 12) and (j - i >= 1):
      soma += matriz
      acc += 1

if sinal == "S":
  print("%.1f" % (soma))
elif sinal == "M":
  print("%.1f" % (soma / acc))
