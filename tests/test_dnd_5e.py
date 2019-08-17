import random

from dnd_5e import __version__, create_character
from dnd_5e.classes import Fighter
from dnd_5e.races import Human
from dnd_5e.character import Character, AbilityScores


def test_version():
    assert __version__ == "0.1.0"


def test_create_character():
    character = create_character(clazz=Fighter, race=Human)

    assert isinstance(character, Fighter)
    assert isinstance(character, Human)
    assert isinstance(character, Character)


def test_generate_ability_scores():
    random.seed(1234)
    new_ability_scores = AbilityScores()
    x = new_ability_scores.generate_ability_value()

    assert x == 10


def test_generate_ability_scores():
    random.seed(1234)
    new_ability_scores = AbilityScores()

    assert new_ability_scores.strength == 10
    assert new_ability_scores.dexterity == 15
    assert new_ability_scores.constitution == 14
    assert new_ability_scores.intelligence == 13
    assert new_ability_scores.wisdom == 15
    assert new_ability_scores.charisma == 16
