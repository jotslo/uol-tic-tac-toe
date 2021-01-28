from modules.generic import *
from time import sleep
from random import randint

class Game:
    def __init__(self):
        # declare initial variables for game
        self.mode = "Multiplayer"
        self.board = [" " for i in range(9)]
        self.turn = 1
    

    def player_move(self):
        print(f"It's Player {self.turn}'s turn. Type a number from 1-9 to move.")
        move = input("\n> ")
        
        # check if move is valid digit from 1-9
        if move.isdigit():
            move_int = int(move)
            if move_int in range(1, 10):

                # if slot not taken on board, update board and set turn
                if self.board[move_int - 1] == " ":
                    self.board = functions.draw_board(
                        self.board, move_int, data.num_to_marker[self.turn]
                    )
                    self.turn = 2 if self.turn == 1 else 1


    def run(self):
        # run game until winner is declared or draw
        while not functions.get_winner(self.board):
            functions.clear_display()
            functions.print_board(self.board)

            # request player's move, regardless of marker
            self.player_move()
        
        # clear display, output final board and get winner
        functions.clear_display()
        functions.print_board(self.board)
        winner = functions.get_winner(self.board)

        # reset game info, output winner
        self.__init__()
        if winner == "DRAW":
            print("It's a draw!")
        else:
            print(f"Player {winner} has won!")
        
        # request input to return to main menu
        input("Press any key to return to the main menu.\n\n> ")