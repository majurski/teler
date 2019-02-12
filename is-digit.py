A = input()
B = []
for i in A:
    if i.isdigit():
        B.append(int(i))

print(sum(B))