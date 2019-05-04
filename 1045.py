a,b,c = map(float,input().split())
lista = []
lista.append(a)
lista.append(b)
lista.append(c)

lista.sort(reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]

if a>= (b+c):
  print("NAO FORMA TRIANGULO")
else:
  if (a**2) == ((b**2)+(c**2)):
    print("TRIANGULO RETANGULO")
  if (a**2) > ((b**2) + (c**2)):
    print("TRIANGULO OBTUSANGULO")
  if (a**2) < ((b**2)+(c**2)):
    print("TRIANGULO ACUTANGULO")
  if a == b == c:
    print("TRIANGULO EQUILATERO")
  elif a == b:
    print("TRIANGULO ISOSCELES")
  elif a == c:
    print("TRIANGULO ISOSCELES")
  elif b == c:
    print("TRIANGULO ISOSCELES")a, b, c = map(float, input().split())
lista = [a, b, c]
lista.sort(reverse = True)
lista = a[0]
lista = b[1]
lista = c[2]

if (c < a + b) and (b < c + a) and (a < b + c):
   if ((a * a) == (b * b) + (c * c)):
       print("TRIANGULO RETANGULO")
   if ((a * a) > (b * b) + (c * c)):
       print(" TRIANGULO OBTUSANGULO")
   if ((a * a) < (b * b) + (c * c)):
       print("TRIANGULO ACUTANGULO")
   if (a == b == c):
       print("TRIANGULO EQUILATERO")
   if (a == b) or (b == c) or (a == c):
       print("TRIANGULO ISOSCELES")
       
elif: a>=(b+c):
    print("NAO FORMA TRIANGULO")