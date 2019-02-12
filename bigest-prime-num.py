#number = int(input())
n = 120

A = [True for a in range(2,n)]
i=0
j=0
m=0
while i < int(n**0.5):
   i+= 1
   if A[i] == True:
      while j < n:
         j = (i**2)+m*i
         #print(j)
         A[j] = False
print(A)
