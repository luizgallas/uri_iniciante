while True:
    x, y = sorted(list(map(int, input().split())))
    soma = 0
    if(x < 1 or y < 1):
        break
    resposta = []
    for i in range(x, (y + 1)):
        soma += i
        resposta.append(i)
    resultado = " ".join(map(str, resposta))
            
    print(resultado,"Sum=%d"%(soma))
             
