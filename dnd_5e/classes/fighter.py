from random import randint

from dnd_5e.classes.clazz import Clazz
from dnd_5e.status import Status


class Fighter(Clazz, Status):
    def second_wind(self) -> None:
        self.add_health(randint(1, 10) + self.level)

    def __init__(self) -> None:
        super().__init__()
        self.level: int = 1
        self.hit_dice: int = 10
        self.proficiency_bonus: int = 2
