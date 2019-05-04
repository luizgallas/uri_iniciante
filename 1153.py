valor = int(input())
conta = valor
while valor > 1:
    conta *= valor - 1
    valor -= 1
print(conta)

