a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

if (c < a + b) and (b < c + a) and (a < b + c) and (0 < a,b,c < 10**5):
    if((a != b and b == c) or ( a == c and a != b) or ( a == b and c != b)):
        print("Valido-Isoceles")
        if ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2)):
            print("Retangulo: S")
        elif ((a**2 != b**2 + c**2) or (b**2 != a**2 + c**2) or (c**2 != b**2 + a**2)):
            print("Retangulo: N")
            
    elif (a == b == c):
        print("Valido-Equilatero")
        if ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2)):
            print("Retangulo: S")
        elif ((a**2 != b**2 + c**2) or (b**2 != a**2 + c**2) or (c**2 != b**2 + a**2)):
            print("Retangulo: N")
               
    elif (a != b != c):
        print("Valido-Escaleno")
        if ((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2)):
            print("Retangulo: S")
        elif ((a**2 != b**2 + c**2) or (b**2 != a**2 + c**2) or (c**2 != b**2 + a**2)):
            print("Retangulo: N")        
else:
    print("Invalido")
    




    
        
    