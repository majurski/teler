N = int(input())
a = []
for i in range(1,N+1):
    if i % 3 and i % 7:
        a.append(str(i))
    else:
        None
print(' '.join(a))

