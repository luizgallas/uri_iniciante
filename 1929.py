a, b, c, d = map(int, input().split())

lista = [a, b, c, d]
d = max(lista)
lista.remove(d)

if (a < b + c) and (b < a + c) and (c < b + a):
    print("S")
else:
    print("N")