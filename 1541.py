chave = 9999
while True:
    chave = input().split()
    if chave == ["0"]:
        break
    medida1, medida2, percent = map(int, chave)
    terreno = ((medida1 * medida2) * 100 / percent) ** 0.5
    print(int(terreno))
    
    
    






