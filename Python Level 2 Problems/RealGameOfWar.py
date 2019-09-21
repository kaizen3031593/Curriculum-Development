import random
import time

p1count = 26
p2count = 26
totalcount = 0 #counts total number of plays
fastForward = False #a boolean that controls whether we run time.sleep() or not

deck = []
for i in range(1,14):
  for j in range(4):
    deck.append(i)
p1stack = []
p2stack = []
random.shuffle(deck) #shuffles deck

#sends cards to each player
for i in range(len(deck)):
  if i%2==0:
    p1stack.append(deck[i])
  else:
    p2stack.append(deck[i])

#prints the cards as strings
def printcard(card):
  if card == 1:
    return("Ace")
  elif card <=10:
    return(str(card))
  elif card == 11:
    return("Jack")
  elif card == 12:
    return("Queen")
  elif card == 13:
    return("King")
  
while p1count>0 and p2count>0:
  p1 = p1stack.pop(0) #pop removes from stack at index provided

  p2 = p2stack.pop(0)
  
  print("Player 1 plays: "+str(printcard(p1)))
  print("Player 2 plays: "+str(printcard(p2)))

  #time.sleep() only called while fast forward has not been selected
  if fastForward == False:
    time.sleep(1)

  pot = [] #stores potential winnings
  pot.append(p1)
  pot.append(p2)
  
  #enter the while loop if the cards are the same and both decks have enough cards for WAR
  while p1==p2 and len(p1stack)>=4 and len(p2stack)>=4: 
    print("Both sides play the same card! Get ready for WAR!\n")

    p1 = p1stack[3] #references the card at that location without popping
    p2 = p2stack[3]
    p1war = p1stack[:4] #player 1's down cards
    p2war = p2stack[:4] #player 2's down cards
    pot += p1war + p2war #adds all 8 additional cards to the pot

    #removes the cards that were added to the pot
    p1stack = p1stack[4:] 
    p2stack = p2stack[4:]

    if fastForward == False:
      time.sleep(1)
    
    #prints out the cards that have been played
    print("Player 1 puts down these 3 cards: ", end="")
    for i in range(3):
      print(p1war[i],end=" ")
    print(" ")
    if fastForward == False:
      time.sleep(2)
    print("Player 2 puts down these 3 cards: ", end="")
    for i in range(3):
      print(p2war[i],end=" ")
    print("\n")

    if fastForward == False:
      time.sleep(2)

    #tells user the final card that matters
    print("Player 1 played " + str(p1) + " and player 2 played " + str(p2))

    if fastForward == False:
      time.sleep(2)

  #break out of the game if p1 still equals p2. That's because either len(p1stack)>=4 or len(p2stack)>=4 is false.
  if p1 == p2:
    break

  print("Cards in the pot: ", end= "")
  printlist=""
  for i in range(len(pot)):
    printlist += printcard(pot[i]) + " "
  print(printlist)
  if fastForward == False:
    time.sleep(1)
  
  #checks to see who wins and adds/subtracts the appropriate number to the total number of cards in each deck.
  if p2>p1:
    p2stack.extend(pot)
    p1count-=int(len(pot)/2) #pot is always even
    p2count+=int(len(pot)/2)
    totalcount+=1
    print("Player 2 takes the cards\n")
    if fastForward == False:
      time.sleep(1)
  elif p1 > p2:
    p1stack.extend(pot)
    p1count+=int(len(pot)/2)
    p2count-=int(len(pot)/2)
    totalcount+=1
    print("Player 1 takes the cards\n")
    if fastForward == False:
      time.sleep(1)

  print("player 1 has: " + str(p1count) + " cards and player 2 has: " + str(p2count) + " cards\n") 
  if fastForward == False:
    time.sleep(1)

  #checks to see if user wants to fast forward
  if fastForward == False:
    check = input("Press 0 to fast forward. Enter to keep going.")
    if check == '0':
      fastForward = True

#whoever has the most cards is the winner
if p1count>p2count:
  print("player 1 wins!")
else:
  print("player 2 wins!")
print("the total number of plays was:" + str(totalcount))