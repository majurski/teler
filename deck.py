N = int(input())
deck = ["2","3","4","5","6","7","8","9","10","J","D","K","A"]
newdeck = []
index = 0

for i in range(1,N):
   newdeck.append(deck[index])
   index+=1

def com():
   for a in newdeck:
      print("{0} of spades, {1} of clubs, {2} of hearts, {3} of diamonds".format(a,a,a,a))


com()