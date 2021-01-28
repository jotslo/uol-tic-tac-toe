from modules.generic import data
from os import system

def print_board(board):
    # iterates through board list and outputs formatted board
    for i in range(0, 9, 3):
        print("|" + "|".join(board[i:i+3]) + "|")
    print()


def draw_board(board, position, marker):
    # update board with marker and return
    board[position-1] = marker
    #print_board(board)
    return board


def get_winner(board):
    # iterate through winning combo positions
    for marker in ["X", "O"]:
        for pos in data.winners:

            # if all positions have same marker, player has won
            if all(board[value] == marker for value in pos):
                return data.marker_to_num[marker]
    
    # check whether board is full, declare draw if so
    if all(marker != " " for marker in board):
        return "DRAW"

    # no players have won, continue game
    return False


def clear_display():
    # execute cls to clear display
    system("cls")


def deepcopy(lst):
    # generate new list replicating original to avoid rewriting
    return [value for value in lst]