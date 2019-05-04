while True:
    try:
        
        teste = int(input())
        senha = teste - 1
        print(senha)
    except EOFError:
        break