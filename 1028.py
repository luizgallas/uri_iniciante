num = int(input())
for i in range(num):
    ricardo, vicente = map(int, input().split())

    if (ricardo > vicente):
        maiorpilha = max(ricardo, vicente)
        menorpilha = min(ricardo, vicente)

    else:
        maiorpilha = min(ricardo, vicente)
        menorpilha = max(ricardo, vicente)

    while maiorpilha % menorpilha != 0:
        divisao = maiorpilha % menorpilha
        maiorpilha = menorpilha
        menorpilha = divisao

    print(menorpilha)
