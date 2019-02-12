from math import sin

N = float(input())
M = float(input())
P = float(input())

chis = N*N + 1/M/P + 1337
	
znam = N - 128.523123123*P
	
pluz = sin(int(M % 180))

a = chis/znam + pluz

print(round(a,6))
