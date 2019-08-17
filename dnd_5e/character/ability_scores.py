from random import randint
from typing import Union


class AbilityScores:
    def generate_ability_value(self) -> int:
        values = sorted([randint(1, 6) for _ in range(6)])
        return sum(values[3:])

    def __init__(
        self,
        strength: Union[int, None] = None,
        dexterity: Union[int, None] = None,
        constitution: Union[int, None] = None,
        intelligence: Union[int, None] = None,
        wisdom: Union[int, None] = None,
        charisma: Union[int, None] = None,
    ) -> None:
        self.strength = strength or self.generate_ability_value()
        self.dexterity = dexterity or self.generate_ability_value()
        self.constitution = constitution or self.generate_ability_value()
        self.intelligence = intelligence or self.generate_ability_value()
        self.wisdom = wisdom or self.generate_ability_value()
        self.charisma = charisma or self.generate_ability_value()
