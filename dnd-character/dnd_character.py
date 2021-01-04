from random import randint
from math import ceil


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        points = [randint(1, 6) for dice in range(4)]
        return sum(points) - min(points)


def modifier(value):
    return (value - 10)//2
