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

#Simple AI algorithm - program just plays a spot randomly.
def randomPlayerMove(board):
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
  #user goes
  if player=='X':
    #while loop to make sure user puts in valid numbers
    while True:
      row=int(input("Pick a row to play: "))
      column = int(input("Pick a column to play: "))
      if -1<row<3 and -1<column<3 and board[row][column]==" ":
        board[row][column]=player
        break
      print("Not a valid move, try again")
  #computer goes
  if player=='O':
    time.sleep(1)
    play=randomPlayerMove(board)
    board[play[0]][play[1]]=player
  #check if someone has won
  if win(board,player):
    break
  #check if all game spots are taken
  if finished(board):
    tie=True
    break
  #changes turns
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
    print("Well, the Random Player Won")