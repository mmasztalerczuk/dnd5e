from dnd_5e.Dice import Dice
from .weapon import Weapon


class Dagger(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.dices = [Dice(4)]
        self.ranged = False
