#above
N = int(input())

w, h = N, N; 
Matrix = [[2**(x+1) for x in range(w)] for y in range(h)] 
    
print(Matrix)   