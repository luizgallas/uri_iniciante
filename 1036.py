import math

n1, n2, n3 = map(float, input().split())

if n1 != 0:
    delta = (n2 * n2) - (4 * n1 * n3)
    if (delta >= 0):
        raiz1 = (-n2 + math.sqrt(delta)) / (2 * n1)
        raiz2 = (-n2 - math.sqrt(delta)) / (2 * n1)
        print("R1 = {:.5f}".format(raiz1))
        print("R2 = {:.5f}".format(raiz2))
    elif (delta < 0):
        print("Impossivel calcular")
else:
    print("Impossivel calcular")




    