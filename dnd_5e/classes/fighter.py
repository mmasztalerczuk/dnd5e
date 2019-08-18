from enum import Enum
from random import randint

from dnd_5e.classes.clazz import Clazz
from dnd_5e.status import Status
from dnd_5e.weapons.fists import Fists


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

    def get_armor_bonus(self, armor):
        if armor is not None and Fighter.FightingStyle.Defense in self.fighting_styles:
            return 1
        return 0

    def get_bonus_dmg(self, main_weapon, second_weapon):
        if main_weapon is not None and not main_weapon.ranged and isinstance(second_weapon,
                                                                             Fists) and \
                Fighter.FightingStyle.Dueling in self.fighting_styles:
            return 2
        return 0
