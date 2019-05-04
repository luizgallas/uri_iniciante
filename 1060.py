numeros = []
soma = 0

numeros.append(float(input()))
numeros.append(float(input()))
numeros.append(float(input()))
numeros.append(float(input()))
numeros.append(float(input()))
numeros.append(float(input()))

for n in numeros:
    if(float(n) > 0):
        soma += 1
        media =  / soma
        
print(soma,"valores positivos")
print(media)