dia1, dia2 = map(int, input().split())

if dia2>=0 and dia2<=2:
    print("nova")

elif dia2<=100 and dia2>=97:
    print("cheia")

elif dia2 > dia1:
    print("crescente")

else:
    print("minguante")