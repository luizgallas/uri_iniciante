
num = float(input())
print("N[%d] = %d" % (0, num))

for i in range(1, 100):
    num /= 2
    print("N[%d] ="%(i), end="")
    print(" {:.4f}".format(num))
    print("")