import math

key = int(input())
for i in range(key):
    num = int(input())
    raiz = int(math.sqrt(num)) + 1
    primo = True if num > 1 else False
    for j in range(2, raiz):
        if num % j == 0:
            primo = False
            break
    if primo:
        print(num,"eh primo")        
    else:
        print(num,"nao eh primo")