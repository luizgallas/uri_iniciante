numero = int(input())
for i in range(numero):
    ano = int(input())
    if ano <= 2014:
        anof = 2015 - ano
        print(anof,"D.C")
    else:
        anof = ano - 2014
        print(anof,"A.C")

            
            