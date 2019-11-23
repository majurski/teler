import math

#Possible combinations n from r
n = 8
r = 3
all = n - r

nf  = math.factorial(n)
rf = math.factorial(r)
allf = math.factorial(all)

s = nf / (rf*allf)
print(round(s))