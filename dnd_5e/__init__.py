__version__ = '0.1.0'


def create_character(clazz, race):
    character = type("Character", (clazz, race), {})
    return character
