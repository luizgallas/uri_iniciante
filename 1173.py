#Trecho do código onde imprime o indice zero, visto que se comecar
#o for com 0, a sequencia nao fica correta
num = int(input())
print("N[%d] = %d" % (0, num))

#Faz o for, atribui 2 ao valor de num e faz o
#mesmo print do indice 0 porem com indice i
for i in range(1, 10):
    num *= 2
    print("N[%d] = %d" % (i, num))