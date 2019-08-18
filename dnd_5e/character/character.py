from typing import Union, Type

from ..races import Race
from ..classes import Clazz
from . import AbilityScores


class Character:
    def __init__(
        self,
        name: str,
        clazz: Clazz,
        race: Race,
        abilities_score: Union[AbilityScores, None] = None,
    ) -> None:
        self.clazz = clazz
        self.race = race

        self.name: str = name
        self.exp: int = 0
        self.abilities_score: AbilityScores = abilities_score or AbilityScores()
