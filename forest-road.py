#geeko
N = int(input())
mah = []
for i in range(0, 2*N-1):
    mah.append([])
    for j in range(0, N):
       mah[i].append([])
       mah[i][j] = "."

for m in range(0,N):
   mah[m][m] = "*"

for b in range(0,N-1):
   mah[N+b][N-(b+2)] = "*"

for i in mah:   
    print(''.join(i))