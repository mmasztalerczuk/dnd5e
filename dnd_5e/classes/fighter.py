from enum import Enum
from random import randint

from dnd_5e.classes.clazz import Clazz
from dnd_5e.situation.situation import Situation
from dnd_5e.status import Status
from dnd_5e.weapons.fists import Fists
from dnd_5e.weapons.shield import Shield


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

        self.action_surge_usage = 0
        self.action_surge_active = True

    def reset_action_surge(self):
        if 2 <= self.level < 17:
            self.action_surge_usage = 1
        elif self.level >= 17:
            self.action_surge_usage = 2
        else:
            self.action_surge_usage = 0

    def do_long_rest(self):
        self.reset_action_surge()

    def do_short_rest(self):
        self.reset_action_surge()

    def new_turn(self):
        self.action_surge_active = True

    def action_surge(self):
        self.action_surge_active = False
        self.actions += 1

    def additional_actions(self):
        if self.action_surge_active and self.action_surge_usage > 0:
            return ["Action Surge"]

    def two_weapon_attack_disabled(self):
        return Fighter.FightingStyle.TwoWeaponFighting in self.fighting_styles

    def attack_roll_bonus(self, weapon):
        if weapon.ranged and Fighter.FightingStyle.Archery in self.fighting_styles:
            return 2
        return 0

    def get_armor_bonus(self, armor):
        if armor is not None and Fighter.FightingStyle.Defense in self.fighting_styles:
            return 1
        return 0

    def get_bonus_dmg(self, main_weapon, second_weapon):
        if (
            main_weapon is not None
            and not main_weapon.ranged
            and isinstance(second_weapon, Fists)
            and Fighter.FightingStyle.Dueling in self.fighting_styles
        ):
            return 2
        return 0

    def do_reaction(self, situation, second_weapon):
        if (
            situation.type == Situation.Type.Attack
            and situation.whom is not self
            and isinstance(second_weapon, Shield)
            and Fighter.FightingStyle.Protection in self.fighting_styles
        ):
            return Situation.Type.Disadvantage

    def reroll_dices(self, main_weapon, dices):
        if (
            main_weapon.two_handed
            and Fighter.FightingStyle.GreatWeaponFighting in self.fighting_styles
        ):
            for dice in dices:
                if dice.result <= 2:
                    dice.roll()
