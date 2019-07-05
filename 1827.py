while True:
    try:
        num = int(input())
        #para fazer o quadrado feito com os 1s começarem no lugar
        #certo
        quad = int(num / 3)
        #ajusta o tamanho do quadrado dos 1
        e = num - quad

        # Preenche com 0
        matriz = [[0 for i in range(num)] for j in range(num)]

        # Preenche com  2
        for i in range(num):
            matriz[i][i] = 2

        # Preenche com 3
        j = 0
        for i in range(num - 1, -1, -1):
            matriz[j][i] = 3
            j += 1

        # Preenche com 1
        for i in range(quad, e):
            for j in range(quad, e):
                matriz[i][j] = 1

        #COloca o 4 no centro da matriz
        matriz[int(num / 2)][int(num / 2)] = 4

        for i in range(num):
            for j in range(num):
                print(matriz[j][i], end='')
            print()
        print()

    except EOFError:
        break