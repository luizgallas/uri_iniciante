diai = int(input())
horario1 = input().split(" : ")
diaf = int(input())
horario2 = input().split(" : ")

hora1 = int(horario1[0])
min1 = int(horario1[1])
seg1 = int(horario1[2])

hora2 = int(horario2[0])
min2 = int(horario2[1])
seg2 = int(horario2[2])


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



