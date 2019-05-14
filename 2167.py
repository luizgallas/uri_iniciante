def queda(lista):
    for i in range(1, len(lista)):
        if lista[i]<lista[i-1]:
            return i+1
    return 0

n = int(input())
r = list(map(int, input().split()))
print(queda(r))