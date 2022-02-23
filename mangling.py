
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display(self):
        print('Nane :', self.name)
        print('Level:', self.level)

    def level_up(self, number):
        self.level += number
        self.__check_level()

    def __check_level(self):
        if self.level > 10:
            self.level = 10

ply1 = Player("test", 5)
ply1.display()
ply1.level_up(4)
ply1.display()
ply1.level_up(100)
ply1.display()
