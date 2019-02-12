N = input()

deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
 
if N in deck:
    print("yes {0}".format(N))
else:
    print("no {0}".format(N))
