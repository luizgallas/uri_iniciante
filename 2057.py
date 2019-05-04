saida, tempo, fuso = input().split(" ")
saida = int(saida)
tempo = int(tempo)
fuso = int(fuso)

resposta = (24 + saida + tempo + fuso)%24
print(resposta)






