#taino

A = input()

B = ''.join(x for x in A if x.isalpha())

print(B[::-1])