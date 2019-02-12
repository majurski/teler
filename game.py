from itertools import combinations

N = input()

digit = []
for i in N:
  digit.append(i.split())
    
comb = []

#A +* B +* C

C = combinations(digit,3)
for n in C:    
    comb.append(n)

print(comb)

