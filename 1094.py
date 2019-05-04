rato = 0
coelho = 0
sapo = 0
caso = int(input())
for i in range(caso):
    quantia, tipo = input().split()
    quantia = int(quantia)
    if tipo == "C":
       coelho += quantia
    elif tipo == "R":
        rato += quantia
    elif tipo == "S":
        sapo += quantia
total = coelho + rato + sapo

print("Total: %d cobaias" %(total))
print("Total de coelhos:", coelho)
print("Total de ratos:", rato)
print("Total de sapos:", sapo)

print("Percentual de coelhos: %.2f %%"%((coelho / total) * 100))
print("Percentual de ratos: %.2f %%"%((rato / total) * 100))
print("Percentual de sapos: %.2f %%"%((sapo / total) * 100))
    
    
        
    
    