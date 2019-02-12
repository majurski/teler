N = int(input())

def fac(n): 
   num = 1 
   while n >= 1: 
      num = num * n 
      n = n - 1 
   return num

part1 = fac(2*N)
part2 = fac(N+1)*fac(N)

cata = part1/part2

print(round(int(cata),2))