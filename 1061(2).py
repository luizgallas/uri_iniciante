dia1 = input().split()
diai = int(dia1[1])

dados1 = input().split(" : ")
hora1, min1, seg1 = list(map(int, dados1))


dia2 = input().split()
diaf = int(dia2[1])

dados2 = input().split(" : ")
hora2, min2, seg2 = list(map(int, dados2))


diatotal = diaf - diai

horatotal = hora2 - hora1
if (horatotal < 0):
    horatotal = 24 + horatotal
    diatotal = diatotal - 1

mintotal = min2 - min1
if (mintotal < 0):
    mintotal = 60 + mintotal
    horatotal = horatotal - 1
    
segtotal = seg2 - seg1
if (segtotal < 0):
    segtotal = 60 + segtotal
    mintotal = mintotal - 1
    
if (diatotal <= 0):
    diatotal = 0
    
print(diatotal, "dia(s)")
print(horatotal, "hora(s)")
print(mintotal, "minuto(s)")
print(segtotal, "segundo(s)")