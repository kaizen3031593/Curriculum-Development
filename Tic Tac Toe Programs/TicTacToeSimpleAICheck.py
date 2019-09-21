import random
import time

def printBoard(board):
  for i in range(3):
    for j in range(3):
      if j==2:
        print(" " + board[i][j], end="")
      else:
        print(" " + board[i][j] + " |", end="")
    if i!=2:
      print("\n ––––––––––")
  print("\n")

def win(board,player):
  #horizontal wins
  if board[0][0]==player and board[0][1]==player and board[0][2]==player:
    return True
  if board[1][0]==player and board[1][1]==player and board[1][2]==player:
    return True
  if board[2][0]==player and board[2][1]==player and board[2][2]==player:
    return True
  #vertical wins
  if board[0][0]==player and board[1][0]==player and board[2][0]==player:
    return True
  if board[0][1]==player and board[1][1]==player and board[2][1]==player:
    return True
  if board[0][2]==player and board[1][2]==player and board[2][2]==player:
    return True
  #diagonal wins
  if board[0][0]==player and board[1][1]==player and board[2][2]==player:
    return True
  if board[0][2]==player and board[1][1]==player and board[2][0]==player:
    return True
  return False

def AIPlayerMove(board):
  #if center is open, play it
  if board[1][1]==" ":
    return[1,1]
  else:
    #check for immediate winning moves
    for i in range(3):
      for j in range(3):
        if testWin(board,i,j,"O") == True:
          return[i,j]
    #check for opponent winning moves
    for i in range(3):
      for j in range(3):
        if testWin(board,i,j,"X") == True:
          return[i,j]
    #play randomly
    while True:
      row=random.randint(0,2)
      column=random.randint(0,2)
      if board[row][column]==' ':
        break
    return [row,column]

def testWin(board,i,j,player):
  duplicate = []
  for a in range(3):
    line = []
    for b in range(3):
      line.append(board[a][b])
    duplicate.append(line)
  if duplicate[i][j]!=" ":
    return False
  duplicate[i][j]=player
  return win(duplicate,player)

def RandomPlayerMove(board):
  while True:
    row=random.randint(0,2)
    column=random.randint(0,2)
    if board[row][column]==' ':
      return [row,column]

def finished(board):
  for i in range(3):
    for j in range(3):
      if board[i][j]==' ':
        return False
  return True

ties=0
randomPlay=0
computer=0

for q in range(1000):
  board = []
  for i in range(3):
    line = []
    for j in range(3):
      line.append(' ')
    board.append(line)
  tie=False
  player='X'
  flip= random.randint(1,2)
  if flip==1:
    player='O'
  while True:
    if player=='X':
      play=RandomPlayerMove(board)
      board[play[0]][play[1]]=player
    if player=='O':
      play=AIPlayerMove(board)
      board[play[0]][play[1]]=player
    if win(board,player):
      break
    if finished(board):
      tie=True
      break
    if player=='X':
      player='O'
    else:
      player='X'

  #printBoard(board)
  if tie:
    ties+=1
  else:
    if player=='X':
      randomPlay+=1
    else:
      computer+=1
print("TIES "+ str(ties))
print("RANDOM WINS "+ str(randomPlay))
print("COMPUTER WINS " + str(computer))