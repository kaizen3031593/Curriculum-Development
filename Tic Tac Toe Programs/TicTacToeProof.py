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

def AIPlayerMove(board):
  #check for a move that wins
  for i in range(3):
    for j in range(3):
      if testWin(board,i,j,"O") == True:
        return[i,j]
  #check for a move that the opponent can play and immediately win
  for i in range(3):
    for j in range(3):
      if testWin(board,i,j,"X") == True:
        return[i,j]
  #check for a move that results in a fork
  for i in range(3):
    for j in range(3):
      if testFork(board,i,j,'O') == True:
        return[i,j]
  #check for a move that the opponent can play and result in a fork. If two forks however, choose to go on the offense
  loseForks=0
  tempSet=[0,0]
  for i in range(3):
    for j in range(3):
      if testFork(board,i,j,'X') == True:
        loseForks+=1
        tempSet=[i,j]
  if loseForks==1:
    return tempSet
  #if 2 forks, choose to force opponent move right away
  elif loseForks==2: 
    if board[0][1]==' ':
      return[0,1]
    if board[1][0]==' ':
      return[1,0]
    if board[1][2]==' ':
      return[1,2]
    if board[2][1]==' ':
      return[2,1]
  #check center
  if board[1][1]==" ":
    return[1,1]
  #check corners
  if board[0][0] == ' ':
    return [0,0]
  if board[0][2]== ' ':
    return[0,2]
  if board[2][0]== ' ':
    return[2,0]
  if board[2][2]== ' ':
    return[2,2]
  #check sides
  if board[0][1]==' ':
    return[0,1]
  if board[1][0]==' ':
    return[1,0]
  if board[1][2]==' ':
    return[1,2]
  return[2,1]

def testWin(board,i,j,player):
  newBoard=duplicateBoard(board)
  if newBoard[i][j]!=" ":
    return False
  newBoard[i][j]=player
  return win(newBoard,player)

def win(board,player):
  if board[0][0]==player and board[0][1]==player and board[0][2]==player:
    return True
  if board[1][0]==player and board[1][1]==player and board[1][2]==player:
    return True
  if board[2][0]==player and board[2][1]==player and board[2][2]==player:
    return True
  if board[0][0]==player and board[1][0]==player and board[2][0]==player:
    return True
  if board[0][1]==player and board[1][1]==player and board[2][1]==player:
    return True
  if board[0][2]==player and board[1][2]==player and board[2][2]==player:
    return True
  if board[0][0]==player and board[1][1]==player and board[2][2]==player:
    return True
  if board[0][2]==player and board[1][1]==player and board[2][0]==player:
    return True
  return False

def duplicateBoard(board):
  duplicate = []
  for a in range(3):
    line = []
    for b in range(3):
      line.append(board[a][b])
    duplicate.append(line)
  return duplicate

def testFork(board,i,j,player):
  newBoard=duplicateBoard(board)
  if newBoard[i][j]!=" ":
    return False
  newBoard[i][j]=player
  winningMoves=0
  for a in range(3):
    for b in range(3):
      if newBoard[a][b]==" ":
        newBoard[a][b]=player
        if win(newBoard,player):
          winningMoves+=1
        newBoard[a][b]=" "
  if winningMoves>=2:
    return True
  return False

def RandomPlayerMove(board):
  while True:
    row=random.randint(0,2)
    column=random.randint(0,2)
    if board[row][column]==' ':
      break
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

  if tie:
    ties+=1
  else:
    if player=='X':
      randomPlay+=1
      printBoard(board)
    else:
      computer+=1

print("TIES "+ str(ties))
print("RANDOM WINS "+ str(randomPlay))
print("COMPUTER WINS " + str(computer))