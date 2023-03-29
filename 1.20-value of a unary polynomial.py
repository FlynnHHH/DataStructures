import sys
lstin = []
try:
    while True:
        row = sys.stdin.readline().strip()
        if row == '':
            break
        row_list = list(map(int, row.split()))
        lstin.extend(row_list)  
except:
    pass
x_0 = lstin[0]
n = lstin[1]
p = 0
for i in range(n + 1):
    p += lstin[i + 2] * x_0 ** i
print(p)
