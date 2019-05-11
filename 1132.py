x = int(input())
y = int(input())
lista = [x, y]
x = min(lista)
y = max(lista)

soma = 0
for i in range(x, y + 1):
    if i % 13 != 0:
        soma += i
print(soma)