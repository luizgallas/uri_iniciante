cha = int(input())
a, b, c, d, e = map(int, input().split())
acc = 0
if a == cha:
    acc += 1
if b == cha:
    acc += 1
if c == cha:
    acc += 1
if d == cha:
    acc += 1
if e == cha:
    acc += 1
print(acc)
    