from enum import Enum


class Situation:
    class Type(Enum):
        Attack = (1,)
        Disadvantage = (2,)

    def __init__(self, type, who, whom=None):
        self.type = type
        self.who = who
        self.whom = whom
