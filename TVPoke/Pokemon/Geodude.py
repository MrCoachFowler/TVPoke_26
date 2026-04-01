from TVPoke.BaseClasses.PokeTypes import Ground
from TVPoke.BaseClasses.Move import Move

class Geodude(Ground):
    def __init__(self):
        moves = [
            Move("Body Slam", "NORMAL", 40),
            Move("Punch", "NORMAL", 20),
            Move("Earthquake", "NORMAL", 15),
            Move("Crunch", "NORMAL", 10)
        ]
        super().__init__("Geodude", 40, moves, "./TVPoke/Pokemon/imgs/Geodude.png")