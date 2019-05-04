aba, acoes = map(int, input().split())
for i in range(acoes):
    acao = input()
    if acao == "fechou":
        aba += 1
    elif acao == "clicou":
        aba -= 1
        
print(aba)