caso = int(input())
for i in range(caso):
    svence = 0
    rvence = 0
    s, r = map(str, input().split())
    if s == r:
        win = 'De novo!'

    elif s == 'tesoura':
        if r == 'papel' or r == 'lagarto':
            win = s
        else:
            win = r
    elif s == 'papel':
        if r == 'pedra' or r == 'Spock':
            win = s
        else:
            win = r
    elif s == 'pedra':
        if r == 'lagarto' or r == 'tesoura':
            win = s
        else:
            win = r
    elif s == 'lagarto':
        if r == 'Spock' or r == 'papel':
            win = s
        else:
            win = r
    elif s == 'Spock':
        if r == 'tesoura' or r == 'pedra':
            win = s
        else:
            win = r
    if win == s:
        win = 'Bazinga!'
    elif win == r:
        win = "Raj trapaceou!"
    print("Caso #%i:"%(i + 1), win)