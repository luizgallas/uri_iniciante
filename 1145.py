x, y = map(int, input().split())

acc = 1
for i in range(1, (y+1)):
    if acc < x:
        print(i, end=" ")
        acc += 1
        continue
    print(i)
    acc = 1