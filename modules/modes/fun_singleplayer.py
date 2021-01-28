from modules.generic import *
from time import sleep
from random import randint, choice

class Game:
    def __init__(self):
        # declare initial variables for game
        self.mode = "Fun Singleplayer"
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
                        self.turn = 2
    

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
                    self.turn = 2


    def player_move(self):
        # output turn instructions and check for first inputted letter
        print(data.player_turn.format("your"))
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
    

    def get_next_bot_move(self):
        # create var to check for move with most possible wins, iterate through all 1-9 moves
        move_wins = []
        move_win_markers = []
        for move in range(1, 10):

            # if board position is empty, add move_wins var, replicate board
            if self.board[move - 1] == " ":
                move_wins.append(0)
                move_win_markers.append(0)
                test_board = functions.deepcopy(self.board)

                # if adding new marker gets a win, set move_wins as low value to prioritise move
                for marker in ["O", "X"]:
                    test_board[move - 1] = marker
                    if functions.get_winner(test_board):
                        move_wins[-1] -= 20000
                        move_win_markers[-1] = marker
                        continue
                
                    # otherwise, iterate through 2nd layer of possible moves
                    test_board[move - 1] = marker
                    for move2 in range(1, 10):
                        if test_board[move2 - 1] == " ":
                            test_board2 = functions.deepcopy(test_board)
                            test_board2[move2 - 1] = marker

                            # if move gets a win, switch to opposite marker to attempt to block
                            if functions.get_winner(test_board2):
                                if move_win_markers[-1] != data.opposite_marker[marker]:
                                    move_win_markers[-1] = data.opposite_marker[marker]
                                
                                # if opposite marker is still invalid, give a lower score
                                else:
                                    move_wins[-1] -= 100
            
            # if board position is taken, set move_wins to high value to prevent overwriting
            else:
                move_wins.append(10000)
                move_win_markers.append(" ")
        
        # sort move_wins in ascending order to find worst bot move, unless next move is a win
        # this prevents the bot from giving the player an opportunity to win next turn
        sorted_wins = sorted(move_wins)#, reverse = True)
        highest_value = sorted_wins[0]

        # if no moves are prioritised, get random move to prevent repetitive moves
        if highest_value == 0:
            player_first_move = "X" if self.board.count("X") else "O"
            random_move = self.board.index(player_first_move)

            # iterate until valid random move found and return
            while self.board[random_move] != " " or move_wins[random_move] < 0:
                random_move = randint(0, 8)
            return data.opposite_marker[player_first_move], random_move + 1
        
        # otherwise, return prioritised marker and move
        best_move = move_wins.index(sorted_wins[0])
        best_marker = move_win_markers[best_move]
        return best_marker, best_move + 1
    

    def bot_move(self):
        # wait 1-2 seconds to replicate player thinking
        move_speed = randint(10, 20) / 10
        move_int = randint(0, 8)
        print("It's the bot's turn. Thinking...\n\n> ", end="")
        sleep(move_speed)

        # get bot's next move
        best_marker, move_int = self.get_next_bot_move()
        
        # slot not taken on board, update board and set marker
        self.board = functions.draw_board(
            self.board, move_int, best_marker
        )


    def run(self):
        # run game until winner is declared or draw
        while not functions.get_winner(self.board):
            functions.clear_display()
            functions.print_board(self.board)

            # if turn is player 1, request player's turn type
            if self.turn == 1:
                self.player_move()
                
            # otherwise, request bot's turn type
            elif self.turn == 2:
                self.bot_move()
                self.turn = 1
        
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