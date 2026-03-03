from TVPoke.BaseClasses.PokeTypes import Grass, Poison
from TVPoke.BaseClasses.Move import Move

class Gloom(Grass, Poison):
    def __init__(self):
        moves = [
            Move("Absorb", "NORMAL", 60),
            Move("Leaf Storm", "NORMAL", 80),
            Move("Poison Powder", "WATER", 80),
            Move("Acid", "NORMAL", 0)
        ]
        super().__init__("Gloom", 140, moves, "./TVPoke/Pokemon/imgs/Feraligatr.png")