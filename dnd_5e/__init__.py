from typing import Any, Type

from dnd_5e.character import Character
from dnd_5e.classes import Clazz
from dnd_5e.races import Race

__version__ = "0.1.0"


def create_character(clazz: Type[Clazz], race: Type[Race]) -> Any:
    new_character = type("Character", (clazz, race, Character), {})
    return new_character()
