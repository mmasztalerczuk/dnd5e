from typing import Union, Type, Any

from ..races import Race
from ..classes import Clazz
from . import AbilityScores


def create_character(
    clazz: Type[Clazz],
    race: Type[Race],
    name: str,
    abilities_score: Union[AbilityScores, None] = None,
) -> Any:
    class Character(clazz, race):  # type: ignore
        def __init__(self) -> None:
            super().__init__()
            self.name: str = name
            self.exp: int = 0
            self.abilities_score: AbilityScores = abilities_score or AbilityScores()

            self.current_health: int = self.max_health

        def add_health(self, health: int) -> None:
            self.current_health += health
            if self.current_health > self.max_health:
                self.current_health = self.max_health

        @property
        def max_health(self) -> int:
            return self.hit_dice + AbilityScores.get_ability_modifier(  # type: ignore
                self.abilities_score.constitution
            )

    return Character()
