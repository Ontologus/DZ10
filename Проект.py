import random

def draw_board(board):
  print('-------------')
  print('| ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' |')
  print('----+---+----')
  print('| ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' |')
  print('----+---+----')
  print('| ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' |')
  print('-------------')

def get_player_move(board, player):
  while True:
    print(f'Игрок {player}, через пробел введите строку и столбец вашего хода (отсчёт начинается с левого верхнего угла)')
    try:
      row, column = map(str, input().split())
    except:
      print('Вы неправильно ввели значение хода, посмотрите на условия ввода и введите ещё раз')
      continue
    move = [int(row) - 1, int(column) - 1]
    if int(row) <= 3 and int(column) <= 3 and board[int(row) - 1][int(column) - 1] == ' ':
      return move
    else:
      print('Недопустимый ход. Попробуйте ещё раз')

def get_computer_move(board):
  while True:
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    move = [row, column]
    if board[int(row)][int(column)] == ' ':
      return move

def check_win(board, player):
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] == player:
      return True
    if board[0][i] == board[1][i] == board[2][i] == player:
      return True
    if board[0][0] == board[1][1] == board[2][2] == player:
      return True
    if board[0][2] == board[1][1] == board[2][0] == player:
      return True
    return False

def main():
  board = [[' '] * 3 for i in range(3)]
  print('Добро пожаловать в крестики-нолики.')
  player_choice = input('Вы будете ходить первыми или вторыми? Введите 1 или 2. ')
  if player_choice.isdigit:
    if int(player_choice) == 1 or 2:
      if int(player_choice) == 1:
        players = ['X', 'O']
      elif int(player_choice) == 2:
        players = ['O', 'X']
    else:
      print('Выбор некорректен, вам присвоено значение по умолчанию, вы будете играть за X')
      players = ['X', 'O']
  else:
    print('Выбор некорректен, вам присвоено значение по умолчанию, вы будете играть за X')
    players = ['X', 'O']
  turn = 0
  while True:
    draw_board(board)
    player = players[turn % 2]
    if player == 'X':
      move = get_player_move(board, player)
    else:
      print(f'Компьютер {player} делает ход')
      move = get_computer_move(board)
    board[move[0]][move[1]] = player
    one_dimensional_board = []
    for i in range(3):
      for j in range(3):
        one_dimensional_board.append(board[i][j])
    if check_win(board, player):
      draw_board(board)
      print(f'Поздравляем, {player} победил!')
      break
    elif ' ' not in one_dimensional_board:
      if not(check_win(board, player)):
        draw_board(board)
        print('К сожалению, у вас ничья')
        break
      else:
        print(f'Поздравляем, игрок {player} победил!')
        break
    turn += 1
main()