from random import randint
from typing import Union, Type, Any

from dnd_5e.classes import Fighter
from dnd_5e.weapons.fists import Fists
from dnd_5e.weapons.shield import Shield
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

            self.actions = 1
            self.speed = 30
            self.bonus_action = 1
            self.reaction = 1

            self.set_main_weapon(Fists())
            self.set_second_weapon(Fists())

            if fighting_style:
                self.fighting_styles.append(fighting_style)

        def add_health(self, health: int) -> None:
            self.current_health += health
            if self.current_health > self.max_health:
                self.current_health = self.max_health

        def get_number_of_actions(self):
            return 1 + self.additional_actions()

        def set_main_weapon(self, weapon):
            self.main_weapon = weapon
            if self.main_weapon.two_handed:
                self.second_weapon = weapon

        def reaction(self, situation):
            return self.do_reaction(situation, second_weapon=self.second_weapon)

        def set_second_weapon(self, weapon):
            self.second_weapon = weapon

        def get_armor_class(self):
            dex_mod = AbilityScores.get_ability_modifier(self.abilities_score.dexterity)
            if self.armor is None:
                ac = 10 + dex_mod
            else:
                ac = self.armor.get_ac(dex_mod)

            ac += self.get_armor_bonus(self.armor)

            if isinstance(self.second_weapon, Shield):
                ac += 2

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

        def damage_roll(self, two_weapon_attack=False):
            bonus_dmg = 0
            if two_weapon_attack:
                damage_dices = self.second_weapon.get_damage()
            else:
                damage_dices = self.main_weapon.get_damage()

            if self.main_weapon.ranged:
                weapon_modifier = AbilityScores.get_ability_modifier(
                    self.abilities_score.dexterity
                )
            else:
                weapon_modifier = AbilityScores.get_ability_modifier(
                    self.abilities_score.strength
                )

            if two_weapon_attack:
                if not self.two_weapon_attack_disabled():
                    weapon_modifier = 0

            bonus_dmg += self.get_bonus_dmg(self.main_weapon, self.second_weapon)

            self.reroll_dices(self.main_weapon, damage_dices)

            damage_roll = 0
            for dice in damage_dices:
                damage_roll += dice.result
            return damage_roll + weapon_modifier + bonus_dmg

        @property
        def max_health(self) -> int:
            return self.hit_dice + AbilityScores.get_ability_modifier(  # type: ignore
                self.abilities_score.constitution
            )

    return Character()
