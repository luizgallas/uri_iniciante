a, b, c = map(int, input().split())

ab = (a + b + abs(a - b)) // 2

abc = (ab + c + abs(ab - c)) // 2

print(abc, "eh o maior")