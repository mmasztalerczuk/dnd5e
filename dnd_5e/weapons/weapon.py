class Weapon:
    def __init__(self):
        self.dices = []
        self.ranged = False
        self.two_handed = False

    def get_damage(self) -> int:
        total_dmg = []
        for dice in self.dices:
            dice.roll()
            total_dmg.append(dice)

        return total_dmg
