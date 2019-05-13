num = int(input())
for i in range(num):
    n1, n2 = map(int, input().split())
    calculo = n1 ** n2
    print(len(str(calculo)))
