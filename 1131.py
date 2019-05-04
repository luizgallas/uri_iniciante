fim = 1
vgremio = 0
vinter = 0
empate = 0
final = 0
soma = 0
while (fim == 1):
    inter, gremio = map(int, input().split())
    soma += 1
    if inter > gremio:
        vinter = vinter + 1
    elif gremio > inter:
        vgremio = vgremio + 1
    elif inter == gremio:
        empate += 1
    
        
    
    print("Novo grenal (1-sim 2-nao)")
    fim = int(input())
    
    
print(soma,"grenais")
print("Inter:%d" %(vinter))
print("Gremio:%d" %(vgremio))
print("Empates:%d" %(empate))
if vinter > vgremio:
    print("Inter venceu mais")
elif vgremio > vinter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
    