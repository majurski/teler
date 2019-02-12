A = input()
B = input()

if A == "text":
    print((B)+"*")
elif A == "real":
    print(round(float(B)+1,2))
elif A == "integer":
    print(int(float(B)+1))