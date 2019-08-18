import random

from dnd_5e import __version__
from dnd_5e.classes import Fighter
from dnd_5e.races import Human
from dnd_5e.character import AbilityScores, create_character
from dnd_5e.weapons.fists import Fists
from dnd_5e.weapons.longbow import LongBow


def test_version():
    assert __version__ == "0.1.0"


def test_create_character():
    random.seed(1234)

    name = "my name"
    character = create_character(clazz=Fighter, race=Human, name=name,
                                 fighting_style=Fighter.FightingStyle.Defense)

    assert character.hit_dice == 10
    assert character.proficiency_bonus == 2
    assert character.exp == 0
    assert character.name == name
    assert character.speed == 30
    assert character.fighting_styles == [Fighter.FightingStyle.Defense]


def test_fighter_second_wind():
    random.seed(1234)

    name = "my name"
    character = create_character(clazz=Fighter, race=Human, name=name)
    character.current_health = 5

    character.second_wind()

    assert character.current_health == 8


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


def test_fighter():
    new_fighter = Fighter()
    assert new_fighter.hit_dice == 10
    assert new_fighter.proficiency_bonus == 2


def test_human():
    new_human = Human()
    assert new_human.speed == 30


def test_attack_roll():
    random.seed(1234)

    name = "my name"
    character = create_character(clazz=Fighter, race=Human, name=name)

    assert character.attack_roll() == 3


def test_set_bow_as_weapon():
    random.seed(1233)
    new_ability_scores = AbilityScores(dexterity=10)
    name = "my name"
    character = create_character(clazz=Fighter, race=Human, name=name, abilities_score=new_ability_scores)
    longbow = LongBow()
    character.set_main_weapon(longbow)

    assert character.main_weapon == longbow
    assert character.attack_roll() == 12
    assert character.damage_roll() == 4


def test_fists_as_weapon():
    name = "my name"
    new_ability_scores = AbilityScores(strength=10)

    character = create_character(clazz=Fighter, race=Human, name=name, abilities_score=new_ability_scores)

    assert isinstance(character.main_weapon, Fists)
    assert character.damage_roll() == 1
