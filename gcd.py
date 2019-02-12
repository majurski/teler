a,b = input().split()
a = int(a)
b = int(b)
def gcd(a, b): 
   while b: 
      a, b = b, a % b 
   return a

print(gcd(a,b))