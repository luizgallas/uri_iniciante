numeros = []
soma = 0

numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))

for n in numeros:
    if (n % 2 == 0):
        soma += 1
        
print(soma, "valores pares")