val1, val2 = map(int, input().split())
duracao = 0

if val1 > val2:
    duracao = (24 - (val1 - val2))
    print("O JOGO DUROU %d HORA(S)" % duracao)
elif val1 < val2:
    duracao = val2 - val1
    print("O JOGO DUROU %d HORA(S)" % duracao)
elif val1 == val2:
    print("O JOGO DUROU 24 HORA(S)")
    