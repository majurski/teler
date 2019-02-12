N = int(input())
arr =  input().split()
#arr = {1,2,3,4,5,7,8,9}

index = 0

even = []
odd = []


for i in range(0,N):
    if index % 2 == 0:
       even.append(arr[index])
    if index % 2 == 1:
       odd.append(arr[index])
    index+=1
        
def mult(a):
   result = 1 
   for x in a:
       x = int(x)
       result = result*x
   return result

evenpro = mult(even)
oddpro = mult(odd)

if evenpro == oddpro:
    print("yes", evenpro)
else:
    print("no",evenpro,oddpro)
