acc = 0
soma = 0

while True:
    idade = int(input())
    if (idade < 0):
        break
    acc += 1
    soma += idade

print("{:.2f}".format(soma / acc))
