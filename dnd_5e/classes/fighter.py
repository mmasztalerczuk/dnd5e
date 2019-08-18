from enum import Enum
from random import randint

from dnd_5e.classes.clazz import Clazz
from dnd_5e.status import Status


class Fighter(Clazz, Status):
    def second_wind(self) -> None:
        self.add_health(randint(1, 10) + self.level)

    class FightingStyle(Enum):
        Archery = (1,)
        Defense = (2,)
        Dueling = (3,)
        GreatWeaponFighting = (4,)
        Protection = (5,)
        TwoWeaponFighting = (6,)

    def __init__(self) -> None:
        super().__init__()
        self.level: int = 1
        self.hit_dice: int = 10
        self.proficiency_bonus: int = 2
        self.fighting_styles = []

    def attack_roll_bonus(self, weapon):
        if weapon.ranged and Fighter.FightingStyle.Archery in self.fighting_styles:
            return 2
        return 0
