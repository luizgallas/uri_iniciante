h1, m1, h2, m2 = map(int, input().split())

horatotal = h2 - h1
mintotal = m2 - m1


if horatotal < 0:
    horatotal += 24

if mintotal < 0:
    mintotal += 60
    horatotal -= 1
    
if mintotal == 0 and horatotal == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(horatotal, mintotal))
    