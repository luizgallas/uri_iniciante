valores = map(lambda x: int(x), input().split(" "))
A, B, C, D = valores

if (B > C) and (D > A) and ((C + D) > (A + B)) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

