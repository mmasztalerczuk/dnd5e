import random

from dnd_5e import __version__
from dnd_5e.classes import Fighter
from dnd_5e.races import Human
from dnd_5e.character import AbilityScores, create_character
from dnd_5e.situation.situation import Situation
from dnd_5e.weapons.dagger import Dagger
from dnd_5e.weapons.fists import Fists
from dnd_5e.weapons.longbow import LongBow
from dnd_5e.weapons.longsword import Longsword
from dnd_5e.weapons.ringmail import RingMail
from dnd_5e.weapons.shield import Shield


def test_version():
    assert __version__ == "0.1.0"


def test_create_character():
    random.seed(1234)

    name = "my name"
    character = create_character(
        clazz=Fighter,
        race=Human,
        name=name,
        fighting_style=Fighter.FightingStyle.Defense,
    )

    assert character.hit_dice == 10
    assert character.proficiency_bonus == 2
    assert character.exp == 0
    assert character.name == name
    assert character.speed == 30
    assert character.fighting_styles == [Fighter.FightingStyle.Defense]
    assert character.get_armor_class() == 12


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
    character = create_character(
        clazz=Fighter, race=Human, name=name, abilities_score=new_ability_scores
    )
    longbow = LongBow()
    character.set_main_weapon(longbow)

    assert character.main_weapon == longbow
    assert character.attack_roll() == 12
    assert character.damage_roll() == 4


def test_set_bow_as_weapon_with_fighting_style():
    random.seed(1233)
    new_ability_scores = AbilityScores(dexterity=10)
    name = "my name"
    character = create_character(
        clazz=Fighter,
        race=Human,
        name=name,
        fighting_style=Fighter.FightingStyle.Archery,
        abilities_score=new_ability_scores,
    )
    longbow = LongBow()
    character.set_main_weapon(longbow)

    assert character.main_weapon == longbow
    assert character.attack_roll() == 14
    assert character.damage_roll() == 4


def test_fists_as_weapon():
    name = "my name"
    new_ability_scores = AbilityScores(strength=10)

    character = create_character(
        clazz=Fighter, race=Human, name=name, abilities_score=new_ability_scores
    )

    assert isinstance(character.main_weapon, Fists)
    assert character.damage_roll() == 1


def test_fists_as_weapon_with_fighting_style():
    name = "my name"
    new_ability_scores = AbilityScores(strength=10)

    character = create_character(
        clazz=Fighter,
        race=Human,
        name=name,
        fighting_style=Fighter.FightingStyle.Archery,
        abilities_score=new_ability_scores,
    )

    assert isinstance(character.main_weapon, Fists)
    assert character.damage_roll() == 1


def test_armor_class():
    name = "my name"
    new_ability_scores = AbilityScores(dexterity=10)

    character = create_character(
        clazz=Fighter, race=Human, name=name, abilities_score=new_ability_scores
    )

    assert character.get_armor_class() == 10


def test_armor_class_fighting_style():
    name = "my name"
    new_ability_scores = AbilityScores(dexterity=10)

    character = create_character(
        clazz=Fighter,
        race=Human,
        name=name,
        fighting_style=Fighter.FightingStyle.Defense,
        abilities_score=new_ability_scores,
    )

    assert character.get_armor_class() == 10


def test_armor_class_with_armor():
    name = "my name"
    new_ability_scores = AbilityScores(dexterity=20)

    character = create_character(
        clazz=Fighter, race=Human, name=name, abilities_score=new_ability_scores
    )
    character.wear_armor(RingMail())

    assert character.get_armor_class() == 14


def test_armor_class_fighting_style_with_armor():
    name = "my name"
    new_ability_scores = AbilityScores(dexterity=20)

    character = create_character(
        clazz=Fighter,
        race=Human,
        name=name,
        fighting_style=Fighter.FightingStyle.Defense,
        abilities_score=new_ability_scores,
    )
    character.wear_armor(RingMail())

    assert character.get_armor_class() == 15


def test_set_dagger_as_weapon():
    random.seed(1233)
    new_ability_scores = AbilityScores(dexterity=10)
    name = "my name"
    character = create_character(
        clazz=Fighter, race=Human, name=name, abilities_score=new_ability_scores
    )
    dagger = Dagger()
    character.set_main_weapon(dagger)

    assert character.main_weapon == dagger
    assert character.attack_roll() == 14
    assert character.damage_roll() == 4


def test_set_dagger_as_weapon():
    random.seed(1233)
    new_ability_scores = AbilityScores(dexterity=10)
    name = "my name"
    character = create_character(
        clazz=Fighter,
        race=Human,
        name=name,
        fighting_style=Fighter.FightingStyle.Dueling,
        abilities_score=new_ability_scores,
    )
    dagger = Dagger()
    character.set_main_weapon(dagger)

    assert character.main_weapon == dagger
    assert character.attack_roll() == 14
    assert character.damage_roll() == 6


def test_set_two_daggers_as_weapon():
    random.seed(1233)
    new_ability_scores = AbilityScores(dexterity=10)
    name = "my name"
    character = create_character(
        clazz=Fighter,
        race=Human,
        name=name,
        fighting_style=Fighter.FightingStyle.Dueling,
        abilities_score=new_ability_scores,
    )
    dagger = Dagger()
    character.set_main_weapon(dagger)
    dagger2 = Dagger()
    character.set_second_weapon(dagger2)

    assert character.main_weapon == dagger
    assert character.second_weapon == dagger2
    assert character.attack_roll() == 14
    assert character.damage_roll() == 4


def test_set_longsword_as_weapon():
    random.seed(1233)
    new_ability_scores = AbilityScores(dexterity=10)
    name = "my name"
    character = create_character(
        clazz=Fighter,
        race=Human,
        name=name,
        fighting_style=Fighter.FightingStyle.Dueling,
        abilities_score=new_ability_scores,
    )
    longsword = Longsword()
    character.set_main_weapon(longsword)

    assert character.main_weapon == longsword
    assert character.second_weapon == longsword


def test_set_longsword_as_weapon_with_great_weapon_fighting_feat():
    random.seed(1234)
    new_ability_scores = AbilityScores(dexterity=10)
    name = "my name"
    character = create_character(
        clazz=Fighter,
        race=Human,
        name=name,
        fighting_style=Fighter.FightingStyle.GreatWeaponFighting,
        abilities_score=new_ability_scores,
    )
    longsword = Longsword()
    character.set_main_weapon(longsword)

    assert character.main_weapon == longsword
    assert character.damage_roll() == 8


def test_set_longsword_as_weapon_with_great_weapon_fighting_feat():
    random.seed(1234)
    new_ability_scores = AbilityScores(dexterity=10)
    name = "my name"
    character = create_character(
        clazz=Fighter, race=Human, name=name, abilities_score=new_ability_scores
    )
    longsword = Longsword()
    character.set_main_weapon(longsword)

    assert character.main_weapon == longsword
    assert character.damage_roll() == 2


def test_set_shield_with_fighting_style():
    random.seed(1234)
    name = "my name"
    character = create_character(
        clazz=Fighter,
        race=Human,
        fighting_style=Fighter.FightingStyle.Protection,
        name=name,
    )
    personA = object()
    personB = object()

    situation = Situation(Situation.Type.Attack, who=personA, whom=personB)

    shield = Shield()
    character.set_second_weapon(shield)

    assert character.second_weapon == shield
    assert character.reaction(situation) == Situation.Type.Disadvantage


def test_set_shield_without_fighting_style():
    random.seed(1234)
    name = "my name"
    character = create_character(clazz=Fighter, race=Human, name=name)
    personA = object()
    personB = object()

    situation = Situation(Situation.Type.Attack, who=personA, whom=personB)

    shield = Shield()
    character.set_second_weapon(shield)

    assert character.second_weapon == shield
    assert character.reaction(situation) is None


def test_dmg_second_weapon():
    random.seed(1233)
    new_ability_scores = AbilityScores(dexterity=10)
    name = "my name"
    character = create_character(
        clazz=Fighter, race=Human, name=name, abilities_score=new_ability_scores
    )
    dagger = Dagger()
    character.set_main_weapon(dagger)
    dagger2 = Dagger()
    character.set_second_weapon(dagger2)

    assert character.main_weapon == dagger
    assert character.second_weapon == dagger2
    assert character.attack_roll() == 14
    assert character.damage_roll(two_weapon_attack=True) == 2


def test_dmg_second_weapon_with_feat():
    random.seed(1233)
    new_ability_scores = AbilityScores(dexterity=10)
    name = "my name"
    character = create_character(
        clazz=Fighter,
        race=Human,
        name=name,
        fighting_style=Fighter.FightingStyle.TwoWeaponFighting,
        abilities_score=new_ability_scores,
    )
    dagger = Dagger()
    character.set_main_weapon(dagger)
    dagger2 = Dagger()
    character.set_second_weapon(dagger2)

    assert character.main_weapon == dagger
    assert character.second_weapon == dagger2
    assert character.attack_roll() == 14
    assert character.damage_roll(two_weapon_attack=True) == 4
