from PyUI.PageElements import *
from PyUI.Screen import Screen
from PyUI.Window import Window

class WinScreen(Screen):
    def __init__(self, window, winningTrainer):  # Add Computer Player When Done!
        super().__init__(window, (30, 0, 90))
        self.state = {
            "goTo": False,
        }
        self.winningTrainer = winningTrainer

        self.elements = [
            Label((50, 90), 50, 50, "Game Over!", 20, (0,255,0)),
            Label((50, 30), 50, 50, ("Winner: "+self.winningTrainer), 20, (255,200,0)), # Replace dummy w/  screen.computerChoice
        ]
        print('WhatTheScreenSaw '+self.winningTrainer) # I dont know why it will sometimes that it recieved 2 answers, and it appears to be ALWAYS sissors. But it works as intended right now so im not going to touch this and let it do its thing.
