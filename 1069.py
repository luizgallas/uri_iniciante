for i in range(int(input())):
    text = input().replace('.', '')
    countOpen = 0
    countDiamonds = 0

    for char in text:
        if char == '<':
            countOpen += 1
        elif char == '>' and countOpen > 0:
            countDiamonds += 1
            countOpen -= 1

    print(countDiamonds)