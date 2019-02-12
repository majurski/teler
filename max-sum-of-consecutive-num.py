A = int(input())
B = []

for i in range(0,A):
    B.append(int(input()))

print(sum(B))

for i in B:
    print(max(B))    
    
itertools.groupby(iterable, key=None)