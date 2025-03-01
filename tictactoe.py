"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
                continue
            if cell == O:
                o_count += 1

    if x_count <= o_count:
        return X
    
    return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))
    
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError('Invalid action!')
    
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # chech if row 0 has tree same value
    if board[0][0] != EMPTY and board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]

    # chech if row 1 has tree same value
    if board[1][0] != EMPTY and board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]

    # chech if row 2 has tree same value
    if board[2][0] != EMPTY and board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]

    # chech if col 0 has tree same value
    if board[0][0] != EMPTY and board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    
    # chech if col 1 has tree same value
    if board[0][1] != EMPTY and board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]

    # chech if col 2 has tree same value
    if board[0][2] != EMPTY and board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]

    # check if letf to right diagonally has tree same value
    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    # check if right to left diagonally has tree same value
    if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    if len(actions(board)) == 0:
        return True

    return False




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    
    if winner(board) == O:
        return -1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
 
    current_player = player(board)

    if current_player == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    else:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            score = max_value(result(board, action))
            if score < best_score:
                best_score = score
                best_action = action
        return best_action


def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

