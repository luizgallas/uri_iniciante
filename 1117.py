soma = 0
quantidade = 0

while quantidade < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        soma += nota
        quantidade += 1
    else:
        print("nota invalida")
    
print("media = {:.2f}".format(soma/2))