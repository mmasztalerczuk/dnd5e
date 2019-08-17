from dnd_5e import __version__, create_character, Character
from dnd_5e.classes import Fighter
from dnd_5e.races import Human
from dnd_5e.character import Character


def test_version():
    assert __version__ == '0.1.0'


def test_create_character():
    character = create_character(clazz=Fighter, race=Human)

    assert isinstance(character, Fighter)
    assert isinstance(character, Human)
    assert isinstance(character, Character)

