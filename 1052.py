calendario = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
mes = int(input()) - 1
if (0 <= mes <= 11):
    print(calendario[mes])