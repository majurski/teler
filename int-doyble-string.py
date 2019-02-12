A = input()

if 65 <= (ord(A[0])) <= 90:
    print((A)+"*")
elif 97 <= (ord(A[0])) <= 122:
    print((A)+"*")
elif 48 <= (ord(A[0])) <= 57:
    print(int(A)+1)
elif A[0] == "-":
    print(float(A)+1)