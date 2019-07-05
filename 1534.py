while True:
    try:
        n = int(input())

        mat = [[0.0] * n for i in range(n)]

        for i in range(0, n):
            for j in range(0, n):
                sec = n - 1

                if n-j-1 == i:
                    mat[i][j] = '2'

                elif i == j:
                    mat[i][j] = '1'

                else:
                    mat[i][j] = '3'

        for i in range(0, n):
            M = ''.join(mat[i])
            print(M)

    except EOFError:
        break