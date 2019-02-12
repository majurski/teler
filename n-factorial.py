N = int(input())

def fac(n): 
   num = 1 
   while n >= 1: 
      num = num * n 
      n = n - 1 
   return num

print(fac(int(N)))