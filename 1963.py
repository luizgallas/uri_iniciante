val1, val2 = map(float, input().split())

if val1 == val2:
    percent = 0
else:
    final = val2 - val1
    percent = (final / val1) * 100

print("{:.2f}%".format(percent))
