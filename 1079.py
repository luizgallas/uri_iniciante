num = int(input())
p1, p2, p3 = 2, 3, 5
ptotal = p1 + p2 + p3
for i in range(num):
    n1, n2, n3 = map(float, input().split())
    media = (n1 * p1 + n2 * p2 + n3 * p3) / ptotal
    print("{:.1f}".format(media))
    
    