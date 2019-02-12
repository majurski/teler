#bonus

N = int(input())

limits = {
	(1,3): 10,
	(4,6): 100,
	(7,9): 1000	
	}

def bon(N):
   for k, v in limits.items():
      if k[0] <= N and N <= k[1]:
        print(N*v)

bon(N)

if N < 0 or N > 9:
    print("invalid score")
