entrada = input().split()
altura = int(entrada[0])
canos = [int(cano) for cano in input().split()]
resultado = "YOU WIN"

for i in range(len(canos) - 1):
    if abs(canos[i+1] - canos[i]) > altura:
        conseguiu = False
        break
print(resultado)
