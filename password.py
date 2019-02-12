#password
N,K = input().split()

K = int(K)

number = []
def ading():
    for i in N:
        number.append(i)
    return number

a = ading()

mem0 = a[0]
mem1 = a[1]
mem2 = a[2]
mem3 = a[3]
mem4 = a[4]
mem5 = a[5]


a[0] = a[5]
a[1] = a[4] 
a[2] = a[3]
a[3] = mem2
a[4] = mem1
a[5] = mem0

a = ''.join(a)
b = int(a)
res = divmod(b,K)

print(sum(res))



