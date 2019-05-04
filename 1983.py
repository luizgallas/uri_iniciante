n_matricula = n_nota = 0
for i in range(int(input())):
    matricula, nota = input().split(" ")
    matricula, nota = int(matricula), float(nota)
    if nota >= 8 and nota > n_nota:
        n_matricula, n_nota = matricula, nota
        
if (n_matricula == 0):
    print("Minimum note not reached")
else:
    print(n_matricula)
        

    
