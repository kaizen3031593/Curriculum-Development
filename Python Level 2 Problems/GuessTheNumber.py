guess = 50
low=0
high=100
numGuess=0
while True:
  guess=int((low+high)/2)
  if numGuess==7:
    print("Is " + str(guess) + " correct? It's definitely right!")
    break
  elif low==high:
    print("Well then " + str(low) + " must be your number!")
    break
  else: 
    answer = input("Is your number " + str(guess) +"? If not, is it above or below " + str(guess) + "?")
  numGuess+=1
  if answer == "above":
    low = guess+1
  elif answer == "below":
    high= guess-1
  else:
    break
  
print("I knew I'd guess it!")
