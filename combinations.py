from itertools import combinations

N, K = input().split()

N = int(N)
K = int(K)

B = []
for i in range(1,N+1):
    B.append(i)

C = combinations(B,K)
for n in C:     
    l = str(n)[1 : -1] 
    a = l.split(",")
    print("".join(a))