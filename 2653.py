joias = []

while True:
    try:
        joia = input()
        joias.append(joia)
    except EOFError:
        break


joias = set(joias)
print(len(joias))