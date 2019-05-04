#Aumento de salários a seus funcionários de acordo com a tabela abaixo
salario = float(input())
salario = ("{:.2f}".format(salario))
salario = float(salario)

#Valores
#Entre 0 e 400
if (salario >= 0) and (salario <= 400.00):
    print("Novo salario: {:.2f}".format(salario + (salario * 0.15)))
    print("Reajuste ganho: {:.2f}".format(salario * 0.15))
    print("Em percentual: 15 %")
#Entre 400,01 e 800
elif (salario >= 400.01) and (salario <= 800.00):
    print("Novo salario: {:.2f}".format(salario + (salario * 0.12)))
    print("Reajuste ganho: {:.2f}".format(salario * 0.12))
    print("Em percentual: 12 %")
#Entre 800.01 e 1200.00
elif (salario >= 800.01) and (salario <= 1200.00):
    print("Novo salario: {:.2f}".format(salario + (salario * 0.10)))
    print("Reajuste ganho: {:.2f}".format(salario * 0.10))
    print("Em percentual: 10 %")
#Entre 1200.01 e 2000.00
elif (salario >= 1200.01) and (salario <= 2000.00):
    print("Novo salario: {:.2f}".format(salario + (salario * 0.07)))
    print("Reajuste ganho: {:.2f}".format(salario * 0.07))
    print("Em percentual: 7 %")
#Acima de 2000.00
elif (salario >= 2000.01):
    print("Novo salario: {:.2f}".format(salario + (salario * 0.04)))
    print("Reajuste ganho: {:.2f}".format(salario * 0.04))
    print("Em percentual: 4 %")
    


