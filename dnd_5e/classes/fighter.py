from dnd_5e.classes.clazz import Clazz


class Fighter(Clazz):
    def __init__(self) -> None:
        self.hit_points_base = 10
        self.hit_points = self.hit_points_base

        self.proficiency_bonus = 2
