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
            self.second_weapon: Weapon = None
            self.armor = None

            self.set_main_weapon(Fists())
            self.set_second_weapon(Fists())

            if fighting_style:
                self.fighting_styles.append(fighting_style)

        def add_health(self, health: int) -> None:
            self.current_health += health
            if self.current_health > self.max_health:
                self.current_health = self.max_health

        def set_main_weapon(self, weapon):
            self.main_weapon = weapon

        def set_second_weapon(self, weapon):
            self.second_weapon = weapon

        def get_armor_class(self):
            dex_mod = AbilityScores.get_ability_modifier(self.abilities_score.dexterity)
            if self.armor is None:
                ac = 10 + dex_mod
            else:
                ac = self.armor.get_ac(dex_mod)

            ac += self.get_armor_bonus(self.armor)

            return ac

        def attack_roll(self):
            attack_roll_bonus = 0

            if self.main_weapon.ranged:
                weapon_modifier = AbilityScores.get_ability_modifier(
                    self.abilities_score.dexterity
                )
            else:
                weapon_modifier = AbilityScores.get_ability_modifier(
                    self.abilities_score.strength
                )

            return (
                randint(1, 20)
                + weapon_modifier
                + attack_roll_bonus
                + self.attack_roll_bonus(weapon=self.main_weapon)
            )

        def wear_armor(self, armor):
            self.armor = armor

        def damage_roll(self):
            bonus_dmg = 0

            if self.main_weapon.ranged:
                weapon_modifier = AbilityScores.get_ability_modifier(
                    self.abilities_score.dexterity
                )
            else:
                weapon_modifier = AbilityScores.get_ability_modifier(
                    self.abilities_score.strength
                )

            bonus_dmg += self.get_bonus_dmg(self.main_weapon, self.second_weapon)

            return self.main_weapon.get_damage() + weapon_modifier + bonus_dmg

        @property
        def max_health(self) -> int:
            return self.hit_dice + AbilityScores.get_ability_modifier(  # type: ignore
                self.abilities_score.constitution
            )

    return Character()
