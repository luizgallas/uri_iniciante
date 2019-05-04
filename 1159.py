while 1:
    n = int(input())
    
    if n == 0:
        break
    
    soma = 0
    for i in range(5):
        while (n % 2 != 0):
            n += 1
        soma += n
        n += 1

    print(soma)