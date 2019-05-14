gritos = 3
soma = 0
while gritos > 0:
    entrada = input()
    if entrada == 'caw caw':
        print(soma)
        soma = 0
        gritos -= 1
        continue

    entrada = int("".join(map(lambda x: '0' if x == '-' else '1', entrada)), 2)
    soma += entrada
