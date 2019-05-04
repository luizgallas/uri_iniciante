numeros = []
soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0

numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))
numeros.append(int(input()))

for n in numeros:
    if (n % 2 == 0):
        soma1 += 1
    if(n % 2 != 0):
        soma2 += 1
    if(n > 0):
        soma3 += 1
    if(n < 0):
        soma4 += 1
                
print(soma1, "valor(es) par(es)")
print(soma2, "valor(es) impar(es)")
print(soma3, "valor(es) positivo(s)")
print(soma4, "valor(es) negativo(s)")


