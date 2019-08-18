from random import randint
from typing import Union, Type, Any

from dnd_5e.classes import Fighter
from dnd_5e.weapons.fists import Fists
from dnd_5e.weapons.weapon import Weapon
from ..races import Race
from ..classes import Clazz
from . import AbilityScores


def create_character(
    clazz: Type[Clazz],
    race: Type[Race],
    name: str,
    fighting_style: Union[Fighter.FightingStyle, None] = None,
    abilities_score: Union[AbilityScores, None] = None,
) -> Any:
    class Character(clazz, race):  # type: ignore
        def __init__(self) -> None:
            super().__init__()
            self.name: str = name
            self.exp: int = 0
            self.abilities_score: AbilityScores = abilities_score or AbilityScores()

            self.current_health: int = self.max_health
            self.main_weapon: Weapon = None
            self.set_main_weapon(Fists())

            if fighting_style:
                self.fighting_styles.append(fighting_style)

        def add_health(self, health: int) -> None:
            self.current_health += health
            if self.current_health > self.max_health:
                self.current_health = self.max_health

        def set_main_weapon(self, weapon):
            self.main_weapon = weapon

        def attack_roll(self):
            if self.main_weapon.ranged:
                weapon_modifier = AbilityScores.get_ability_modifier(self.abilities_score.dexterity)
            else:
                weapon_modifier = AbilityScores.get_ability_modifier(self.abilities_score.strength)

            return randint(1, 20) + weapon_modifier

        def damage_roll(self):
            if self.main_weapon.ranged:
                weapon_modifier = AbilityScores.get_ability_modifier(self.abilities_score.dexterity)
            else:
                weapon_modifier = AbilityScores.get_ability_modifier(self.abilities_score.strength)

            return self.main_weapon.get_damage() + weapon_modifier

        @property
        def max_health(self) -> int:
            return self.hit_dice + AbilityScores.get_ability_modifier(  # type: ignore
                self.abilities_score.constitution
            )

    return Character()
