x = 0
while(x != 2):
    soma = 0
    qntd = 0
    
    while(qntd < 2):
        nota = float(input())
        if (0 <= nota <= 10.0):
            qntd += 1
            soma += nota
        else:
            print("nota invalida")
    print("media = {:.2f}".format(soma/2))
    
    print("novo calculo (1-sim 2-nao)")
    x = int(input())
    if (x == 1):
        continue
    elif (x == 2):
        break
    else:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
        
    
    