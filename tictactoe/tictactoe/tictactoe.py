"""
Tic Tac Toe Player
"""
import copy
import math

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
    x_nb =0
    o_nb = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_nb +=1
            elif board[i][j] == O:
                o_nb += 1
    if x_nb > o_nb :
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))
    return moves


def result(board, action):

    if action not in actions(board):
        raise ValueError("Not valid move")
    copy_board = copy.deepcopy(board)
    copy_board[action[0]][action[1]] = player(board)
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    dial_x , dial_o,diar_x,diar_o = (0,) * 4
    for i in range(3):
        row_x , row_o , col_x , col_o  = (0,)*4

        if board[i][i] == X :
            dial_x +=1
        if board[i][i]== O:
            dial_o += 1
        if board[2-i][i] == X:
            diar_x +=1
        if board[2-i][i] == O:
            diar_o += 1

        for j in range(3):
            if board[i][j] == X:
                col_x += 1
            if board[i][j] == O:
                col_o += 1
            if board[j][i] == X:
                row_x += 1
            if board[j][i] == O:
                row_o += 1
        if dial_x ==3 or row_x ==3 or col_x == 3 or diar_x ==3:
            return X
        elif dial_o ==3 or row_o ==3 or col_o == 3 or diar_o ==3:
            return O
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None  or not any(EMPTY in row for row in board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        r = winner(board)
        if r == X:
            return 1
        elif r == O:
            return -1
        else:
            return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    turn = player(board)
    moves = actions(board)
    best_move ={}
    if turn == X:
        for move in moves :
            best_move[move] = min_value(result(board,move))
        return max(best_move , key=best_move.get )
    elif turn == O :
         for move in moves :
            best_move[move] = max_value(result(board,move))
         return min(best_move,key=best_move.get)


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v ,max_value(result(board,action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v , min_value(result(board,action)))
    return v




