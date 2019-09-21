grid = []
for i in range(10):
  line = []
  for j in range(10):
    line.append(False)
  grid.append(line)

def printBoard(game):
  print(" ", end="")
  for i in range(len(game[0])):
    if i<10:
      print(" "+str(i), end="")
    else:
      print(i, end="")
  print("")

  for x in range(len(game)):
    print(x, end=" ")
    for y in range(len(game[x])):
      #print(y, end ="")
      if game[x][y] == 1:
        print("O", end=" ")
      elif game[x][y] == 2:
        print("X", end=" ")
      else:
        print("-",end=" ")
    print("")

def checkWin(grid,playerTurn):
  for i in range(len(grid)-4):
    for j in range(len(grid[0])-4):
      if grid[i][j]== playerTurn:
        if isWinner(grid,i,j, playerTurn):
          return True
  return False

def isWinner(grid,i,j,p):
  if grid[i][j+1]==p and grid[i][j+2]==p and grid[i][j+3]==p and grid[i][j+4]==p:
    return True
  if grid[i+1][j]==p and grid[i+2][j]==p and grid[i+3][j]==p and grid[i+4][j]==p:
    return True
  if grid[i+1][j+1]==p and grid[i+2][j+2] ==p and grid[i+3][j+3]==p and grid[i+4][j+4]==p:
    return True
  return False

playerTurn = 1
while True: 
  printBoard(grid)
  while True:
    row = int(input("Player " + str(playerTurn) +", please input the row of your next move"))
    column = int(input("Player " + str(playerTurn) +", please input the column of your next move"))
    if -1<row and row<10 and -1<column and column<10 and grid[row][column]!=1 and grid[row][column]!=2:
      break
    print("That was not a valid move! Please try again")
  grid[row][column]=playerTurn
  if checkWin(grid,playerTurn):
    break
  if playerTurn==1:
    playerTurn=2
  else:
    playerTurn=1

printBoard(grid)
print("Congrats, Player " + str(playerTurn) + " has won!")