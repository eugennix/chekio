class Warrior:
    health: int = 50
    attack: int = 5
    is_alive: bool = True

    def hited_check_fatal(self, enemy) -> bool:
        ' :returns True if hit fatal'
        self.health -= enemy.attack
        if self.health < 1:
            self.is_alive = False
            return True
        return False


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    while True:
        if unit_2.hited_check_fatal(unit_1):
            return 1
        if unit_1.hited_check_fatal(unit_2):
            return 0
    return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
