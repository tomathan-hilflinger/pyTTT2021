board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

symbols = ['X', 'O']
turn = 0
rounds = 0

# Prints the board
def print_board():
  for row in board:
    for col in row:
      print(col, end=' ')
    print()

# Inserts a move at a given row & column
def make_move(row, col, symbol):
  board[row][col] = symbol

# Returns true when the game is over 
def is_game_over():
  while rounds != 9:
    #Check to see if someone won each rounds after 5 turns
    if rounds >= 5:
     
      #check vertical win
      if board[0][0] == board[0][1] == board[0][2]:
        return True
      elif board[1][0] == board[1][1] == board[1][2]:
        return True
      elif board[2][0] == board[2][1] == board [2][2]:
        return True
      
      #Checks horizontal win
      elif board[0][0] == board[1][0] == board[2][0]:
        return True
      elif board[0][1] == board[1][1] == board[2][1]:
        return True
      elif board[0][2] == board[1][2] == board[2][2]:
        return True
      
      #Checks diagonal win
      elif board[0][0] == board[1][1] == board[2][2]:
        return True
      elif board[2][0] == board[1][1] == board[0][2]:
        return True
    return False
  print("Game Over")

# Alternates the turn between 0 and 1
def change_turn():
  global turn
  turn = (turn + 1) % 2

while not is_game_over():
  # Print the board and whose turn it is
  print_board()
  print('Player {}'.format(turn+1))

  # Get the user input
  row_choice = int(input('Which row would you like to choose? '))
  col_choice = int(input('Which column would you like to choose? '))

  # Put their move on the board
  make_move(row_choice, col_choice, symbols[turn])
  change_turn()
  rounds += 1