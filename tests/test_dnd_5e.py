from dnd_5e import __version__, Warrior


def test_version():
    assert __version__ == '0.1.0'


def test_create_character():
    name = "My Name"
    character = Warrior(name=name)

    assert character.name == name


