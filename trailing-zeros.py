N = int(input())
def trailing_zeros_of_factorial(n): 
   assert n >= 0, n 
   zeros = 0 
   q = n
   
   while q: 
      q //= 5 
      zeros += q 
   
   return zeros

print(trailing_zeros_of_factorial(N)) # => 7