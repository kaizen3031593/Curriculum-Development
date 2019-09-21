import random
import time

board = []
for i in range(3):
  line = []
  for j in range(3):
    line.append(' ')
  board.append(line)

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

#AI is better than random now. Will check if it has a winning move and play it. It will also check if opponent has a winning move and play it to block as well.
def AIPlayerMove(board):
  #if center is open, play it.
  if board[1][1]==" ":
    return[1,1]
  else:
    #check if AI has any moves that result in a win
    for i in range(3):
      for j in range(3):
        if testWin(board,i,j,"O") == True:
          return[i,j]
    #checks if opponent has any moves that result in a win
    for i in range(3):
      for j in range(3):
        if testWin(board,i,j,"X") == True:
          return[i,j]
    #plays random move if can't find anything else
    while True:
      row=random.randint(0,2)
      column=random.randint(0,2)
      if board[row][column]==' ':
        break
    return [row,column]

def testWin(board,i,j,player):
  #create a new board and add the potential next move
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

def RandomPlayerMove():
  row=random.randint(0,2)
  column=random.randint(0,2)
  return [row,column]

def finished(board):
  for i in range(3):
    for j in range(3):
      if board[i][j]==' ':
        return False
  return True

input("Welcome to Tic-Tac-Toe. Press Enter to start.")
tie=False
player='X'
flip=random.randint(1,2)
if flip==1:
  print("The coin flip shows that the computer (O) goes first!")
  player='O'
if flip==2:
  print("The coin flip shows that you (X) will go first!")
while True:
  printBoard(board)
  #user moves
  if player=='X':
    while True:
      row=int(input("Pick a row to play: "))
      column = int(input("Pick a column to play: "))
      if 0<=row<=2 and 0<=column<=2 and board[row][column]==" ":
        board[row][column]=player
        break
      print("Not a valid move, try again")
  #computer moves
  if player=='O':
    time.sleep(1)
    play=AIPlayerMove(board)
    board[play[0]][play[1]]=player
  #checks if someone has won
  if win(board,player):
    break
  #checks if board is complete for a tie
  if finished(board):
    tie=True
    break
  #switches turns
  if player=='X':
    player='O'
  else:
    player='X'

printBoard(board)
if tie:
  print("Well, there was a tie!")
else:
  if player=='X':
    print("Wow! You Won!")
  else:
    print("Well, the Computer Won")