qntd_traducoes = int(input())
dict = {}

for i in range(qntd_traducoes):
    lingua = input()
    traducao = input()
    dict[lingua] = traducao

qntd_criancas = int(input())
for i in range(qntd_criancas):
    nome = input()
    lingua = input()
    print(nome)
    print(dict[lingua])
    print()
