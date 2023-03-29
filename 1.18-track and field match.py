import sys
lstin = []
try:
    while True:
        row = sys.stdin.readline().strip()
        if row == '':
            break
        row_list = list(row.split())
        lstin.append(row_list)  
except:
    pass

score = [[0, 0, 0] for times in range(5)]
for i1 in range(len(lstin)):
    lstin[i1][3] = int(lstin[i1][3])
    if lstin[i1][1] == 'M':
        score[ord(lstin[i1][2]) - ord('A')][0] += lstin[i1][3]
    elif lstin[i1][1] == 'F':
        score[ord(lstin[i1][2]) - ord('A')][1] += lstin[i1][3]
    score[ord(lstin[i1][2]) - ord('A')][2] = score[ord(lstin[i1][2]) -
                                                   ord('A')][0] + score[ord(lstin[i1][2]) - ord('A')][1]
# calculate scores
for i2 in range(len(score)):
    for j in range(3):
        if j == 0 and score[i2][j]:
            print("%s M %d" % (chr(ord('A') + i2), score[i2][j]))
        elif j == 1 and score[i2][j]:
            print("%s F %d" % (chr(ord('A') + i2), score[i2][j]))
        elif j == 2 and score[i2][j]:
            print("%s %d" % (chr(ord('A') + i2), score[i2][j]))
# output
