from math import sqrt

p = [3,5,32,25, 239,11,12,2,2]
all = []

mean = round(sum(p)/len(p),0)
print("mean is", mean)

for i in range(len(p)):
    b = (p[(i-1)] - mean)**2
    all.append(b)
    
vari = sum(all)/len(p)-1
print("All sum", sum(all))
print(vari)
print("Standard dev is:", sqrt(vari))