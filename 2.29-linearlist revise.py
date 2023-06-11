A = list(map(str, input().split(',')))
B = list(map(str, input().split(',')))
C = list(map(str, input().split(',')))
repeat = []
for i in range(len(B)):
    for j in range(len(C)):
        if B[i] == C[j] and B[i] not in repeat:
            repeat.append(B[i])
res = [x for x in A if x not in repeat]
print(*res, sep = ',')