import random


class Warrior:
    def __init__(self, health, punch):
        self.health = health
        self.punch = punch

    def attack(self, unit_health):
        return unit_health - self.punch


unit1 = Warrior(100, 20)
unit2 = Warrior(100, 20)

while True:
    l = [1, 2]
    x = random.choice(l)
    if x == 1:
        unit2.health = unit1.attack(unit2.health)
        print(f"unit1 attacked and unit2 health has {unit2.health}")
        if unit2.health <= 0:
            print("unit1 won")
            break
    else:
        unit1.health = unit2.attack(unit1.health)
        print(f"unit2 attacked and unit1 health has {unit1.health}")
        if unit1.health <= 0:
            print("unit2 won")
            break
