#N = int(input())
#x = int(input)

N = 3
x = 2

def fac(n): 
   num = 1 
   while n >= 1: 
      num = num * n 
      n = n - 1 
   return num


part = fac(N)/x**N
print(part)
def all():
    for i in range(0,N):
        return round(part,5)

resh = 1+ N*all()

print(resh)