import random
import time

deck = []
for i in range(2,14):
  for j in range(0,4):
    card = []
    card.append(i)
    if j==0:
      card.append('Hearts')
    elif j==1:
      card.append('Diamonds')
    elif j==2:
      card.append('Clubs')
    else:
      card.append('Spades')
    deck.append(card)
random.shuffle(deck) #shuffles deck

#prints the cards as strings
def printcard(card):
  result = ""
  #print number
  if card[0] <=10:
    result+= str(card[0])+ " of "
  elif card[0] == 11:
    result+= "Jack of "
  elif card[0] == 12:
    result+= "Queen of "
  elif card[0] == 13:
    result+= "King of "
  elif card[0] == 14:
    result+= "Ace of "
  #print suit
  result+= card[1]
  print (result)

#deal 5 cards
print("your cards...")
time.sleep(1)
hand = [deck.pop(0),deck.pop(0),deck.pop(0),deck.pop(0),deck.pop(0)]
for card in hand:
  printcard(card)
  time.sleep(1)

print("")

def checkRoyalFlush(hand):
  if checkStraightFlush(hand):
    for card in hand:
      if card[0] == 14:
        return True
  return False

def checkStraightFlush(hand):
  return checkStraight(hand) and checkFlush(hand)

def checkFourOfAKind(hand):
  freq = {}
  for card in hand:
        if card[0] in freq:
            freq[card[0]] += 1
        else:
            freq[card[0]] = 1
  for number in freq:
    if freq[number]==4:
      return True
  return False

def checkFullHouse(hand):
  return checkThreeOfAKind(hand) and checkPairs(hand) == 1

def checkFlush(hand):
  suit = hand[0][1]
  for card in hand:
    if card[1] != suit:
      return False
  return True

def checkStraight(hand):
  numbers=[]
  for card in hand:
    numbers.append(card[0])
  numbers.sort()
  a = numbers[0]
  for i in range(len(numbers)):
    if a != numbers[i]:
      return False
    a+=1
  return True

def checkThreeOfAKind(hand):
  freq = {}
  for card in hand:
        if card[0] in freq:
            freq[card[0]] += 1
        else:
            freq[card[0]] = 1
  for number in freq:
    if freq[number]==3:
      return True
  return False

def checkPairs(hand):
  freq = {}
  for card in hand:
        if card[0] in freq:
            freq[card[0]] += 1
        else:
            freq[card[0]] = 1
  pairs = 0
  for number in freq:
    if freq[number]==2:
      pairs+=1
  return pairs

#check all the possible outcomes of 5 cards
if checkRoyalFlush(hand) == True:
    print("You have a royal flush!")
elif checkStraightFlush(hand) == True:
  print("You have a straight flush!")
elif checkFourOfAKind(hand) == True:
  print("You have four of a kind!")
elif checkFullHouse(hand) == True:
  print("You have a full house")
elif checkFlush(hand) == True:
  print("You have a flush!")
elif checkStraight(hand) == True:
  print("You have a straight!")
elif checkThreeOfAKind(hand) == True:
  print("You have three of a kind")
elif checkPairs(hand) == 2:
  print("You have two-pair")
elif checkPairs(hand) == 1:
  print("You have a pair")
else:
  print("You have high card")



'''
if checkRoyalFlush([[14,"Hearts"],[13,"Hearts"],[12,"Hearts"],[11,"Hearts"],[10,"Hearts"]]) == True:
  print("YAYYY")'''
'''
def checkFlush(hand):
  freq = {}
  for card in hand:
        if card[1] in freq:
            freq[card[1]] += 1
        else:
            freq[card[1]] = 1
  for number in freq:
    if freq[number] >=5:
      return True
  return False
'''

