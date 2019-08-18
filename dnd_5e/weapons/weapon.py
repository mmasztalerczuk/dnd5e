class Weapon:
    def __init__(self):
        self.dices = []
        self.ranged = False

    def get_damage(self) -> int:
        total_dmg = 0
        for dice in self.dices:
            total_dmg += dice.roll()

        return total_dmg
