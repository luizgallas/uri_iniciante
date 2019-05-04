salario = float(input())

if (0.00 < salario <= 2000.00):
    print("Isento")
    
elif (2000.00 < salario <= 3000.00):
    valor = salario - 2000
    real = (valor * 8) / 100
    print("R$ {:.2f}".format(real))
    
elif (3000.00 < salario <= 4500.00):
    valor = salario - 2000
    valor2 = valor - 1000
    taxa1 = (1000 * 8) / 100
    taxa2 = (valor2 * 18) / 100
    taxareal = taxa1 + taxa2
    print("R$ {:.2f}".format(taxareal))
    
elif (salario > 4500.00):
    valor = salario - 2000
    valor2 = valor - 1000
    taxa1 = (1000 * 8) / 100
    valor3 = valor2 - 1500
    taxa2 = (1500 * 18) / 100
    taxa3 = (valor3 * 28) / 100
    taxareal = taxa1 + taxa2 + taxa3
    print("R$ {:.2f}".format(taxareal))
    


        
    
    