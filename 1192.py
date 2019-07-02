num = int(input())
for i in range(num):
    casos = input()
    if int(casos[0]) == int(casos[2]):
        resultado = (int(casos[0]) * int(casos[2]))

    elif casos.upper() == casos:
        resultado = int(casos[2]) - int(casos[0])

    elif casos.lower() == casos:
        resultado = int(casos[0]) + int(casos[2])

    print(resultado)