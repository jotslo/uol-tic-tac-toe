from modules.generic import *
from time import sleep
from random import randint

class Game:
    def __init__(self):
        # declare initial variables for game
        self.mode = "Singleplayer"
        self.board = [" " for i in range(9)]
        self.turn = 1
    

    def player_move(self):
        print("It's your turn. Type a number from 1-9 to move.")
        move = input("\n> ")
        
        # check if move is valid digit from 1-9
        if move.isdigit():
            move_int = int(move)
            if move_int in range(1, 10):

                # if slot not taken on board, update board and set marker
                if self.board[move_int - 1] == " ":
                    self.board = functions.draw_board(
                        self.board, move_int, data.num_to_marker[self.turn]
                    )
                    self.turn = 2
    

    def get_next_bot_move(self):
        # create var to check for move with most possible wins, iterate through all 1-9 moves
        move_wins = []
        for move in range(1, 10):

            # if board position is empty, add move_wins var, replicate board
            if self.board[move - 1] == " ":
                move_wins.append(0)
                test_board = functions.deepcopy(self.board)

                # if adding new marker gets a win, set move_wins as high value to prioritise moves
                # if the marker is an "O", set as higher value to prioritise and get bot to win
                # otherwise, the lower value will still be the highest move win
                # which will force bot to block and prevent the player from winning next turn
                for marker in ["O", "X"]:
                    test_board[move - 1] = marker
                    if functions.get_winner(test_board):
                        move_wins[-1] += 2000 if marker == "X" else 20000
                
                # otherwise, iterate through 2nd layer of possible moves
                test_board[move - 1] = "O"
                for move2 in range(1, 10):
                    if test_board[move2 - 1] == " ":
                        test_board2 = functions.deepcopy(test_board)
                        test_board2[move2 - 1] = "O"

                        # if move gets a win, add to move_wins var for the original move
                        if functions.get_winner(test_board2):
                            move_wins[-1] += 1
            
            # if board position is taken, set move_wins value to -1 to prevent overwriting
            else:
                move_wins.append(-1)
        
        # sort move_wins in descending order to find next best bot move
        sorted_wins = sorted(move_wins, reverse = True)
        highest_value = sorted_wins[0]

        # if no moves are prioritised, get random move to prevent repetitive moves
        if highest_value == 0:
            random_move = self.board.index("X")

            # iterate until valid random move found and return
            while self.board[random_move] != " ":
                random_move = randint(0, 8)
            return random_move
        
        # otherwise, return prioritised move
        return move_wins.index(sorted_wins[0]) + 1


    def bot_move(self):
        # wait 1-2 seconds to replicate player thinking
        move_speed = randint(10, 20) / 10
        move_int = randint(0, 8)
        print("It's the bot's turn. Thinking...\n\n> ", end="")
        sleep(move_speed)

        # get bot's next move
        move_int = self.get_next_bot_move()
        
        # slot not taken on board, update board and set marker
        self.board = functions.draw_board(
            self.board, move_int, data.num_to_marker[self.turn]
        )
        self.turn = 1


    def run(self):
        # run game until winner is declared or draw
        while not functions.get_winner(self.board):
            functions.clear_display()
            functions.print_board(self.board)

            # if player 1's turn, request player's move
            if self.turn == 1:
                self.player_move()
                
            # otherwise, request bot's move
            elif self.turn == 2:
                self.bot_move()
        
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