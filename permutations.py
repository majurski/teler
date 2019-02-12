from itertools import permutations
N = int(input())
K = int(input())

B = []
for i in range(1,N+1):
    B.append(i)
    
C = permutations(B, K)
for _ in C:
    l = str(_)[1 : -1] 
    a = l.split(",")
    print("".join(a))