N = int(input())
K = int(input())

def fac(n): 
   num = 1 
   while n >= 1: 
      num = num * n 
      n = n - 1 
   return num

print(int(fac(N)/fac(K)))