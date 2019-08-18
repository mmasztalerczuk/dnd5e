from dnd_5e.Dice import Dice
from .weapon import Weapon


class Fists(Weapon):
    def __init__(self) -> None:
        super().__init__()
        self.dices = [Dice(1)]
