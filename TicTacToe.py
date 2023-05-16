''' BOARD INDEX LAYOUT
      00  |  01  |  02
    --------------------
      10  |  11  |  12
    --------------------
      20  |  21  |  22     '''

from math import inf


def main():
    board = [['', '', 'X'],
            ['', 'X', ''],
            ['O', '', '']]
    player = 'O'
    while True:
       empty_spots_arr = empty_spots(board)
       if is_winner(board, 'O'):
          print("O WON!")
          break
       if is_winner(board, 'X'):
          print("X WON!")
          break
       if not empty_spots_arr:
          print("TIE!")
          break
       best_score = -inf
       for i, j in empty_spots_arr:
          board[i][j] = player
          score = minimax(board, 'X' if player != 'X' else 'O', False)
          if score > best_score:
             best_score = score
             best_move = (i, j)
          board[i][j] = ''
       i, j = best_move
       board[i][j] = player
       player = 'X' if player != 'X' else 'O'
    print_board(board)


# The minimax algorithm
def minimax(board: list[list[str]], player: str, is_maximising: bool) -> int:
    if is_winner(board, player):
       return 1 if is_maximising else -1
    if is_winner(board, 'X' if player != 'X' else 'O'):
       return -1 if is_maximising else 1
    empty_spots_arr = empty_spots(board)
    if not empty_spots_arr:
       return 0
    if is_maximising:
       best_score = -inf
       for i, j in empty_spots_arr:
          board[i][j] = player
          score = minimax(board, 'X' if player != 'X' else 'O', not is_maximising)
          if score > best_score:
             best_score = score
             best_move = (i, j)
          board[i][j] = ''
       return best_score
    else:
       best_score = inf
       for i, j in empty_spots_arr:
          board[i][j] = player
          score = minimax(board, 'X' if player != 'X' else 'O', not is_maximising)
          if score < best_score:
             best_score = score
             best_move = (i, j)
          board[i][j] = ''
       return best_score









# Human friendly print of a board
def print_board(board: list[list[str]]):
    for i in range(3):
       print("  {:1}  |  {:1}  |  {:1}  ".format(board[i][0], board[i][1], board[i][2]))
       if i < 2:
          print("----------------")

# Returns a list of (y,x) tuples representing empty spots for a given board.
def empty_spots(board: list[list[str]]) -> list[tuple[int, int]]:
    empty_spots_arr = []
    for i in range(3):
       for j in range(3):
          if not board[i][j]:
             empty_spots_arr.append((i, j))
    return empty_spots_arr

# Returns rather player won the game or not for a given board.
def is_winner(board: list[list[str]], player: str) -> bool:
    win_patterns = [[board[0][0], board[0][1], board[0][2]],  # Upper row
                    [board[1][0], board[1][1], board[1][2]],  # Middle row
                    [board[2][0], board[2][1], board[2][2]],  # Bottom row
                    [board[0][0], board[1][0], board[2][0]],  # Right column
                    [board[0][1], board[1][1], board[2][1]],  # Middle column
                    [board[0][2], board[1][2], board[2][2]],  # Left column
                    [board[0][0], board[1][1], board[2][2]],  # Main diagonal
                    [board[0][2], board[1][1], board[2][0]]]  # Secondary diagonal
    return ([player] * 3) in win_patterns


if __name__ == '__main__':
    main()
