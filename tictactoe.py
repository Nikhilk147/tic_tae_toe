"""
Tic Tac Toe Player
"""

import math
import copy
from sys import exception

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
    countx = 0
    counto = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countx+=1
            elif board[i][j] == O:
                counto+=1
    if countx > counto:
        return O
    else:
        return X






def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_possible_actions = set()

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == EMPTY:
                all_possible_actions.add((row,column))

    return all_possible_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid action")
    row,column = action
    board_copy = copy.deepcopy(board)
    board_copy[row][column] = player(board)
    return board_copy



def rowcheck(board, player):
    """
    check if elements in a row is same
    """
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    return False

def colcheck(board,player):
    """
    check if elements in column is same
    """
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    return False


def downdiag(board,player):
    """
    check if elements at [0][0], [1][1] and [2][2] are equal to player
    """
    count = 0
    for row in range(len(board)):
        if board[row][row] == player:
            count+1

    if count == 3:
        return True
    else:
        return False


def updiag(board,player):
    """
    check if elements at [0][2], [1][1] and [2][0] are equal to player
    """
    count = 0
    for row in range(len(board)):
        if board[row][len(board) - 1 - row] == player:
            count+1

    if count == 3:
        return True
    else:
        return False





def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if rowcheck(board,X) or colcheck(board,X) or downdiag(board,X) or updiag(board,X):
        return X
    elif colcheck(board,O) or rowcheck(board,O) or downdiag(board,O) or updiag(board,O):
        return O
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) ==X or winner(board) == O:
        return True

    for row in range(len(board)):
        for col  in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    best_action = None
    if current_player == X:
        best_value = -math.inf
        for action in actions(board):
            value = min_value(result(board,action))
            if value > best_value:
                best_value = value
                best_action = action


    elif current_player == O:

        best_value = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action

    return best_action
