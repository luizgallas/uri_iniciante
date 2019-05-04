fim = ""
while (fim == "Sim" or "sim" or "s" or "S"):
    saida, tempo, fuso = input().split(" ")
    saida = int(saida)
    tempo = int(tempo)
    fuso = int(fuso)

    resposta = (24 + saida + tempo + fuso)%24
    print(resposta)
    fim = input("Se deseja continuar digite Sim, caso contrário digite Não.  ")

print("programa encerrado")







