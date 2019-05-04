a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
area = ((a + b) * c) / 2
perimetro = (a + b + c)


if ((a<(b+c)) and (b<(a+c)) and (c<(a+b))):
    print("Perimetro = {:.1f}".format(perimetro))
else:
    print("Area = {:.1f}".format(area))