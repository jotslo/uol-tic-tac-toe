from modules.modes import *
from modules.generic import *

import sys


def quit_game():
    # output goodbye message and exit without error message
    print("Thanks for playing!")
    sys.exit(0)


gamemodes = [
    {"title": "Singleplayer", "input": "s", "run": singleplayer.Game().run, "desc": data.s},
    {"title": "Fun Singleplayer", "input": "fs", "run": fun_singleplayer.Game().run, "desc": data.fs},
    {"title": "Local Multiplayer", "input": "m", "run": multiplayer.Game().run, "desc": data.m},
    {"title": "Fun Multiplayer", "input": "fm", "run": fun_multiplayer.Game().run, "desc": data.fm},
    {"title": "Quit Game", "input": "q", "run": quit_game, "desc": data.q}
]


def get_gamemode(key):
    # iterate through modes, check for matching keys
    for mode in gamemodes:
        if mode["input"] == key:
            return mode


# iterate constantly so user can play multiple times
while True:
    chosen_mode = False
    functions.clear_display()
    print("Noughts & Crosses - Choose a Gamemode\n")

    # iterate through each gamemode and output information
    for mode in gamemodes:
        print(f"{mode['title']} - Enter '{mode['input']}' to select.")
        print(mode['desc'], "\n")

    # keep iterating until mode chosen, get gamemode from key
    while not chosen_mode:
        user_input = input("> ").lower()
        chosen_mode = get_gamemode(user_input)

        # if mode doesn't exist, display error
        if not chosen_mode:
            print("\nInvalid choice, please enter one of the keys shown!")
    
    # mode has been selected, call corresponding function
    chosen_mode["run"]()
