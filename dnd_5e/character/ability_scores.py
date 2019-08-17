from random import randint


class AbilityScores:
    def generate_value(self):
        values = sorted([randint(1, 6) for _ in range(6)])
        return sum(values[3:])

    def __init__(
        self,
        strength=None,
        dexterity=None,
        constitution=None,
        Intelligence=None,
        wisdom=None,
        charisma=None,
    ):
        pass
