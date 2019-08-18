from typing import Union, Type

from ..races import Race
from ..classes import Clazz
from . import AbilityScores


def create_character(
    clazz: Type[Clazz],
    race: Type[Race],
    name: str,
    abilities: Union[AbilityScores, None] = None,
) -> 'Character':

    class Character(clazz, race):
        def __init__(
                self,
                name: str,
                abilities_score: Union[AbilityScores, None] = None,
        ) -> None:
            super().__init__()
            self.clazz = clazz
            self.race = race

            self.name: str = name
            self.exp: int = 0
            self.abilities_score: AbilityScores = abilities_score or AbilityScores()

    return Character(name, abilities_score=abilities)