n = int(input())
acc = 0
for i in range(n):
    cod, qntd = map(int, input().split())
    if cod == 1001:
        conta = qntd * 1.50
        acc += conta
    if cod == 1002:
        conta = qntd * 2.50
        acc += conta
    if cod == 1003:
        conta = qntd * 3.50
        acc += conta
    if cod == 1004:
        conta = qntd * 4.50
        acc += conta
    if cod == 1005:
        conta = qntd * 5.50
        acc += conta

print("{:.2f}".format(acc))
