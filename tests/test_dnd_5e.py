from dnd_5e import __version__, create_character
from dnd_5e.classes import Clazz, Fighter
from dnd_5e.races import Race, Human


def test_version():
    assert __version__ == '0.1.0'


def test_create_character():
    character = create_character(clazz=Clazz.Fighter, race=Race.Human)
    print(type(character))
    assert isinstance(character, Clazz.Fighter)
    assert isinstance(character, Race.Human)

