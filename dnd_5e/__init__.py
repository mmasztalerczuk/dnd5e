from typing import Any, Type, Union

from dnd_5e.character import Character, AbilityScores
from dnd_5e.classes import Clazz
from dnd_5e.races import Race

__version__ = "0.1.0"


def create_character(
    clazz: Type[Clazz],
    race: Type[Race],
    name: str,
    abilities: Union[AbilityScores, None] = None,
) -> Character:

    return Character(name, clazz=clazz(), race=race(), abilities_score=abilities)
