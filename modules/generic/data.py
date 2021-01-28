# this file is used to hold information that seems too extraneous
# to be displayed in the main code file, to ensure the code looks clean

# gamemode descriptions
s =  "Standard noughts and crosses, played against the computer."
m =  "Standard noughts and crosses, played locally with a friend."
fs = """Play either an X or O on your turn, choose whether to add a
new piece to the board or move any existing piece to an empty
location. The player that gets a three-in-a-row first wins!"""
fm = """Play either an X or O on your turn, choose whether to add a
new piece to the board or move any existing piece to an empty
location. The player that gets a three-in-a-row first wins!"""
q =  "Quit the noughts and crosses game."

# long fun mode texts
player_turn = """It's {0} turn!

ADD a new marker to the board - Enter 'a' to select.
MOVE an existing marker on the board - Enter 'm' to select."""

# winning positions
winners = [
    [0, 1, 2], # top row
    [3, 4, 5], # middle row
    [6, 7, 8], # bottom row
    [0, 3, 6], # left column
    [1, 4, 7], # middle column
    [2, 5, 8], # right column
    [0, 4, 8], # left diagonal (\)
    [2, 4, 6]  # right diagonal (/)
]

# default player markers
marker_to_num = {
    "X": 1,
    "O": 2
}
num_to_marker = {
    1: "X",
    2: "O"
}

# opposite markers
opposite_marker = {
    "X": "O",
    "O": "X"
}