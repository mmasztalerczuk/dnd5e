class RingMail:
    def __init__(self):
        self.base_ac = 14
        self.dex_modifier_max = 0

    def get_ac(self, dex_mod):
        return self.base_ac + min(self.dex_modifier_max, dex_mod)
