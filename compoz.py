"""Модуль для вычесления площади комнаты и количества рулонов обоев"""


class WinDoor:
    """Класс окно/дверь"""

    def __init__(self, x, y):
        """Вычесление площади окна/двери"""

        self.square = x * y


class Room:
    """Класс комната"""

    def __init__(self, w, l, h):
        """Инициализатор принимает ширину высоту и длинну"""

        self.width = w
        self.length = l
        self.height = h
        self.wd = []

    def get_all_square(self):
        """Вычесления площади всей комнаты"""

        return 2 * self.height * (self.width + self.length)

    def add_wd(self, x, y):
        """Добавление площадей окон или дверей"""

        self.wd.append(WinDoor(x, y))

    def get_new_square(self):
        """Вычесление нового площади комнаты с учетом вычета площадей дверей и окон"""

        new_square = self.get_all_square()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def get_count_wallpapers(self, l, w):
        """Функция вычесления количества рулонов"""

        check = self.get_new_square()
        counter = 0
        while check > 0:
            check -= l * w
            counter += 1
        return counter


while True:
    print("Enter your numbers or q if you want to quit")
    s = input()
    if s != "q":
        l = []
        s = s.split()
        for i in s:
            if "." in i:
                l.append(float(i))
            else:
                l.append(int(i))
        r1 = Room(*l)
        print("Введите размеры окон или дверей")
        while True:
            win_and_door = input()
            if win_and_door != "q":

                win_and_door = list(map(lambda x: int(x), win_and_door.split()))
                r1.add_wd(*win_and_door)
            else:
                break

        print(r1.get_new_square(), r1.get_count_wallpapers(1, 1))
    elif s == "q":
        break
