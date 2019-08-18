from dnd_5e.races.race import Race


class Human(Race):
    def __init__(self) -> None:
        super().__init__()
        self.speed = 30
