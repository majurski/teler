from itertools import combinations

N = int(input())
K = int(input())

B = []
for i in range(0,N):
    B.append(int(input()))

C = combinations(B,K)
allsums = []
for i in C:
    allsums.append(sum(i))
print(max(allsums))