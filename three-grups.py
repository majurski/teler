arr =  input().split()
#arr = {1,2,3,4,5,7,8,9}

nula = []
edno = []
dve = []


for i in arr:
    i = int(i)
    if i % 3 == 0:
       nula.append(i)
    if i % 3 == 1:
        edno.append(i)
    if i % 3 == 2:
        dve.append(i)

def texi(a):
   l = str(a)[1 : -1] 
   b = l.split(",")
   return "".join(b)
   
print(texi(nula))
print(texi(edno))
print(texi(dve))
