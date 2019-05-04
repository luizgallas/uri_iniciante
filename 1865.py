consegue = 0
teste = int(input())
for i in range(teste):
    nome, forca = (input().split())
    nome = str(nome)
    forca = int(forca)
    if nome != "Thor":
        consegue = False
    elif nome == "Thor":
        consegue = True
    
    if consegue:
        print("Y")
    else:
        print("N")
    
    
    