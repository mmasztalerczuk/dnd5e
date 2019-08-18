from dnd_5e.classes.clazz import Clazz


class Fighter(Clazz):
    def __init__(self) -> None:
        self.hit_dice = 10
        self.proficiency_bonus = 2
