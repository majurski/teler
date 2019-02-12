A = int(input())
B = []

for i in range(0,A):
    B.append(int(input()))


seen = set() 
uniq = [x for x in B if x not in seen and not seen.add(x)] 

print(seen)
    