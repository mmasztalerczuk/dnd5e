from dnd_5e.Dice import Dice
from .weapon import Weapon


class Longsword(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.dices = [Dice(8)]
        self.ranged = False
        self.two_handed = True
