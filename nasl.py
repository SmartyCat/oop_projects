import random


class Soldier:
    def __init__(self, team, rang="soldier"):
        self.number = hash(self)
        self.team = team
        self.rang = rang

    def follow_the_hero(self, obj):
        print(f"I follow for {obj.rang}")


class Hero(Soldier):
    def level_up(self):
        print(f"{self.team} Level was uppgrade")


hero1 = Hero("blue", "King")
hero2 = Hero("red", "Lord")
blue_list = []
red_list = []
for i in range(9):
    l = [1, 2]
    x = random.choice(l)

    if x == 1:
        blue_list.append(Soldier("blue"))
    else:
        red_list.append(Soldier("red"))

if len(blue_list) > len(red_list):
    hero1.level_up()
else:
    hero2.level_up()

blue_list[0].follow_the_hero(hero1)
print(blue_list[0].number)
print(hero1.number)
