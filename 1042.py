#separar os numeros em linhas
numeros = input().split(" ")
a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])
#definir a lista
list = [a, b, c]

#por em ordem crescente
list.sort()

#mostrando os numeros em ordem
print (list[0])
print (list[1])
print (list[2])
print()

#mostrando os valores coletados
print (a)
print (b)
print (c)