lista = []
x = int(input())
y = int(input())
lista.append(x)
lista.append(y)
x = max(lista)
y = min(lista)

for i in range((y + 1), x):
    if (i%5 == 2) or (i%5==3):
        sorted([i])
        print(i)
        