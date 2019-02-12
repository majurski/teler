B = []
C = []

N = int(input())
B.append(input().split())
C.append(input().split())

sums = [ x + y for x, y in zip(B,C)]
print(sums)
    
