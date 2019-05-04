valor = eval(input());

#Para notas de cem
valor = float("%.2f" % valor)
if int(valor / 100) >=1:
    cem = int(valor / 100);
    valor -= cem*100;

valor = float("%.2f" % valor)
if int(valor / 50) >=1:
    cinquenta = int(valor / 50);
    valor -= cinquenta*50;

valor = float("%.2f" % valor)    
if int(valor / 20) >=1:
    vinte = int(valor / 20);
    valor -= vinte*20;

valor = float("%.2f" % valor)
if int(valor/10) >= 1:
 dez = int(valor/10);
 valor -= dez*10.00;

valor = float("%.2f" % valor)
if int(valor / 5) >=1:
    cinco = int(valor / 5);
    valor -= cinco*5;

valor = float("%.2f" % valor)
if int(valor / 2) >=1:
    dois = int(valor / 2);
    valor -= dois*2;

valor = float("%.2f" % valor)
if int(valor / 1) >=1:
    um = int(valor / 1);
    valor -= um*1;

valor = float("%.2f" % valor)
if int(valor / 0.50) >=1:
    cent50 = int(valor / 0.50);
    valor -= cent50*0.50;

valor = float("%.2f" % valor)
if int(valor / 0.25) >=1:
    cent25 = int(valor / 0.25);
    valor -= cent25*0.25;

valor = float("%.2f" % valor)
if int(valor / 0.10) >=1:
    cent10 = int(valor / 0.10);
    valor -= cent10*0.10;

valor = float("%.2f" % valor)
if int(valor / 0.05) >=1:
    cent5 = int(valor / 0.05);
    valor -= cent5*0.05;

valor = float("%.2f" % valor)
if int(valor / 0.01) >=1:
    cent1 = int(valor / 0.01);
    valor -= cent1*0.01;
    
print("NOTAS:");
print(cem, "nota(s) de R$ 100.00")
print(cinquenta, "nota(s) de R$ 50.00")
print(vinte, "nota(s) de R$ 20.00")
print(dez, "nota(s) de R$ 10.00")
print(cinco, "nota(s) de R$ 5.00")
print(dois, "nota(s) de R$ 2.00")
print("MOEDAS:")
print(um, "moeda(s) de R$ 1.00")
print(cent50, "moeda(s) de R$ 0.50")
print(cent25, "moeda(s) de R$ 0.25")
print(cent10, "moeda(s) de R$ 0.10")
print(cent5, "moeda(s) de R$ 0.05")
print(cent1, "moeda(s) de R$ 0.01")
    
    

    










