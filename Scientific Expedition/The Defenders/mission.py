# Taken from mission Army Battles

class Warrior:
    health: int = 50
    attack: int = 5
    is_alive: bool = True

    def hited_check_fatal(self, enemy) -> bool:
        # :returns True if enemy's hit was fatal
        self.health -= enemy.attack
        if self.health < 1:
            self.heath = 0
            self.is_alive = False
            return True
        return False

    def fight(self, unit_2):
        """ return True if self won """
        while True:
            if unit_2.hited_check_fatal(self):
                return 1
            if self.hited_check_fatal(unit_2):
                return 0

class Knight(Warrior):
    attack = 7

class Army():
    def __init__(self):
        self.alive = []
        self.dead = []
        
    def add_units(self, unit_type, num):
        for u in range(num):
            self.alive.append(unit_type())
    
    def get_active(self):
        return self.alive[0]
    
    def active_killed(self):
        self.dead.append(self.alive.pop(0))
    
    def is_any_alive(self):
        return len(self.alive)

class Battle():
    
    def fight(self, a1: Army, a2: Army) -> bool:
        # return True if Army1 won
        while a1.is_any_alive() and a2.is_any_alive():
            a1_war, a2_war = a1.get_active(), a2.get_active()
            if a1_war.fight(a2_war):
                a2.active_killed()
            else:
                a1.active_killed()
        return a1.is_any_alive() > 0

def fight(unit_1, unit_2):
    while True:
        if unit_2.hited_check_fatal(unit_1):
            return 1
        if unit_1.hited_check_fatal(unit_2):
            return 0
    return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
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

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
