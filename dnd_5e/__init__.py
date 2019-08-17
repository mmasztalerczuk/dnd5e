from typing import Any, Type

from dnd_5e.character import Character
from dnd_5e.classes import Clazz
from dnd_5e.races import Race

__version__ = "0.1.0"


def create_character(clazz: Type[Clazz], race: Type[Race], name: str) -> Any:
    def init(self: Character, character_name: str) -> None:
        Character.__init__(self, character_name)

    d = {"__init__": init}

    new_character = type("Character", (Character, clazz, race), d)
    return new_character(name)
