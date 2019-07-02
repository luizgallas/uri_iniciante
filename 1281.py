frutas = []
precos = []
soma = 0

ida = int(input())
for i in range(ida):
    quantidadeprodutos = int(input())
    for i in range(quantidadeprodutos):
        f, p = input().split()
        p = float(p)
        frutas.append(f)
        precos.append(p)

    quantidadecompras = int(input())
    for i in range(quantidadecompras):
        f1, quantidade = input().split()
        quantidade = int(quantidade)

        for i, j in zip(frutas, precos):
            if f1 == i:
                soma = soma + quantidade * j

    print("R$ {:.2f}".format(soma))
    frutas = []
    precos = []
    soma = 0

    