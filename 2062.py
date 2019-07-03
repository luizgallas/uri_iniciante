num = int(input())
palavras = input().split()

uri, obi = "UR", "OB"

palavrasnovas = []
for palavra in palavras:
    if len(palavra) <= 3:
        if palavra[:2] == uri:
            palavra = "URI"
        elif palavra[:2] == obi:
            palavra = "OBI"

    palavrasnovas.append(palavra)

print(" ".join(palavrasnovas))