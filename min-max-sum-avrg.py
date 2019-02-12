N = int(input())

B = []
for i in range(0,N):
    B.append(float(input()))

s = format(min(B),'.2f')
m = format(max(B),'.2f')
h = format(sum(B),'.2f')
z = format(sum(B)/N,'.2f')

print("min="+s)
print("max="+m)
print("sum="+h)
print("avg="+z)