numbers = []
for i in range(100):
    n = int(input())
    numbers.append(n)
    
maior = max(numbers)
pos = numbers.index(maior) + 1
print("%d\n%d" %(maior, pos))