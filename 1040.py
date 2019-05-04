#separar os numeros em linhas
numeros = input().split(" ")
a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])
#definir a lista
list = [a, b, c]

#por em ordem crescente
list.sort()

#mostrando os numeros em ordem
print (list[0])
print (list[1])
print (list[2])

#mostrando os valores coletados
print (a)
print (b)
print (c)





media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10.0
print('Media: {:.1f}'.format (media))

if(media >= 7.0):
    print('Aluno aprovado.');

elif(media < 5.0):
    print('Aluno reprovado.');

elif(media >=5.0) and (media <= 6.9):
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format (exame))
    media2 = (media + exame) / 2
    
    if(media2 >=5.0):
        print('Aluno aprovado.')
        print("Media final: {:.1f}".format (media2))
    
    elif(media2 <= 4.9):
        print('Aluno reprovado.')
        print("Media final: {:.1f}".format (media2))