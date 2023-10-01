def winnerChecker(arr):
    winner = ()
    chk = []
    # checking if column elements are same
    for n in range(3):
        for r in range(3):
            chk.append(arr[r][0][n])
    for i in range(0, len(chk), 3):
        for j in range(i+1, i+2 ):
            if chk[i] == chk[j]:
                if chk[j] == chk[j+1]:
                    winner += chk[i],
                else:
                    break
            else:
                break
    chk.clear()
    
    #checking if row elements are same
    for e in arr:
        if e[0][0] == e[0][1] == e[0][2]:
            if e[0][0] not in winner:
                winner += e[0][0],

    #checking if diagonal elemnents are same
    for r in range(3):
        for c in range(3):
            chk.append(arr[r][0][c])
    if chk[0] == chk[4] == chk[8]:
        if chk[0] not in winner:
            winner += chk[0],
    elif chk[2] == chk[4] == chk[6]:
        if chk[2] not in winner:
            winner += chk[2],
    
    arr.clear()

    if len(winner) == 0 or winner[0] == '.':
        return "DRAW",
    else:
        return winner


arr1 = []
win = ()
for time in range(int(input())):
    for _ in range(3):
        arr1.append(list(map(str, input().split())))
    res = winnerChecker(arr1)
    if res not in win:
        win += res

for w in range(len(win)):
    print(win[w])
