from modules.generic import *
from time import sleep
from random import randint

class Game:
    def __init__(self):
        # declare initial variables for game
        self.mode = "Fun Multiplayer"
        self.board = [" " for i in range(9)]
        self.turn = 1
    

    def add_marker(self):
        # take current marker as input
        print("\nPlease enter the marker you would like to add. (X or O)")
        marker = input("> ").upper()

        # check whether marker is valid and request number from 1-9
        if marker in ["X", "O"]:
            print("\nType a number from 1-9 to place your marker.")
            move = input("> ")

            # check if move is valid digit from 1-9
            if move.isdigit():
                move_int = int(move)
                if move_int in range(1, 10):

                    # if slot not taken on board, update board and set marker
                    if self.board[move_int - 1] == " ":
                        self.board = functions.draw_board(
                            self.board, move_int, marker
                        )
                        self.turn = 1 if self.turn == 2 else 2
    

    def move_marker(self):
        # take current marker and target position as input
        print("\nType a number from 1-9 representing the position of the marker you want to move.")
        original_pos = input("> ")
        print("\nType a number from 1-9 representing the position you want to move the marker to.")
        new_pos = input("> ")

        # check if given positions prepare to validate given values
        if original_pos.isdigit() and new_pos.isdigit():
            orig_pos_int = int(original_pos)
            new_pos_int = int(new_pos)
            pos_range = range(1, 10)

            # if positions are in range from 1-9, check whether marker exists and can be moved
            if orig_pos_int in pos_range and new_pos_int in pos_range:
                original_marker = self.board[orig_pos_int - 1]
                is_valid = (original_marker != " "
                    and self.board[new_pos_int - 1] == " ")

                # if move valid, remove original marker, move to new pos and set turn
                if is_valid:
                    self.board[orig_pos_int - 1] = " "
                    self.board[new_pos_int - 1] = original_marker
                    self.turn = 1 if self.turn == 2 else 2


    def player_move(self):
        # output turn instructions and check for first inputted letter
        print(data.player_turn.format(f"Player {self.turn}'s"))
        move = input("\n> ").lower()
        
        # call function depending on whether player chose "a" or "m"
        if move == "a":
            self.add_marker()
        elif move == "m":
            self.move_marker()
        
        # otherwise, reset output and request markers again
        else:
            functions.clear_display()
            functions.print_board(self.board)
            self.player_move()


    def run(self):
        # run game until winner is declared or draw
        while not functions.get_winner(self.board):
            functions.clear_display()
            functions.print_board(self.board)

            # request player move
            self.player_move()
        
        # clear display, output final board and get winner
        functions.clear_display()
        functions.print_board(self.board)
        winner = functions.get_winner(self.board)

        # output winner and reset game info
        if winner == "DRAW":
            print("It's a draw!")
        else:
            # get winner by checking the previous turn value and output
            print(f"Player {1 if self.turn == 2 else 2} has won!")
        
        # reset data, request input to return to main menu
        self.__init__()
        input("Press any key to return to the main menu.\n\n> ")