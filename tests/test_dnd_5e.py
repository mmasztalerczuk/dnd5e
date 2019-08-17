import random

from dnd_5e import __version__, create_character
from dnd_5e.classes import Fighter
from dnd_5e.races import Human
from dnd_5e.character import Character, AbilityScores


def test_version():
    assert __version__ == "0.1.0"


def test_create_character():
    name = "my name"
    character = create_character(clazz=Fighter, race=Human, name=name)

    assert isinstance(character, Fighter)
    assert isinstance(character, Human)
    assert isinstance(character, Character)
    assert character.hit_points_base == 10
    assert character.hit_points == 10
    assert character.proficiency_bonus == 2
    assert character.exp == 0
    assert character.name == name


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


def test_set_ability_scores():
    random.seed(1234)
    new_ability_scores = AbilityScores(
        strength=2, dexterity=3, constitution=4, intelligence=5, wisdom=6, charisma=7
    )

    assert new_ability_scores.strength == 2
    assert new_ability_scores.dexterity == 3
    assert new_ability_scores.constitution == 4
    assert new_ability_scores.intelligence == 5
    assert new_ability_scores.wisdom == 6
    assert new_ability_scores.charisma == 7


def test_character():
    name = "my_name"
    new_chars = Character(name)
    assert new_chars.exp == 0
    assert new_chars.name == name


def test_fighter():
    new_fighter = Fighter()
    assert new_fighter.hit_points_base == 10
    assert new_fighter.hit_points == 10
    assert new_fighter.proficiency_bonus == 2
