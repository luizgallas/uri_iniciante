
num = int(input())
for i in range(num):
    x, y = map(int, input().split())
    if y == 0:
        print("divisao impossivel")
    else:
        print("{:.1f}".format(x / y))
