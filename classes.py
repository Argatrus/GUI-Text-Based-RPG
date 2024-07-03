import random
multipliers = [0.75, 0.8, 0.85, 0.95, 1, 1.05, 1.1, 1.15]


class Heal:
    def __init__(self, number, master):
        self.n = number
        self.strength = 20
        self.master = master
    
    def __iter__(self):
        return iter([self.n, self.strength])

    def heal(self):
        if self.n > 0:
            self.master.heal(self)
            self.n -= 1
        else:
            return 'nopp'

class SuperHeal(Heal):
    def __init__(self, number):
        super().__init__(number)
        self.strength = 50

class FullHeal(Heal):
    def __init__(self, number, master):
        super().__init__(number)
        self.strength = master.max_health


class Parent: # main parent class for all characters
    def __init__(self, name):
        self.name = name # can name characters (maybe rename)...
        self.exp = [0, 100]
        self.level = 1
        self.max_health = 100
        self.health = 100
        self.attacks = {
            'punch': [5, 100, 9]
        }
        self.armour = [0.9, 100]
        self.heals = [5, 20]
        self.accuracy  = 1
        self.base_heal = Heal(5)
        self.super_heal = SuperHeal(0)
        self.full_heal = FullHeal(0)
    
    def level_up(self):
        self.level += 1
        self.exp = [0, self.exp[1]+20]

    # Going to use a randomiser to handle all combat stuff making it like a classic crpg.

    def take_damage(self, damage):
        self.health -= round(damage *(random.choice(multipliers)*self.armour[0]))
        self.armour[1] -= round(damage * (random.choice(multipliers)*(1-(self.armour[0]))))

    def attack(self, name):
        if self.attacks[name][1] > 0:
            self.attacks[1] -= 1
            return self.attacks[name][0] * random.choice(multipliers) * self.attacks[name][2] * self.accuracy
        else:
            return 'nopp'

    def heal(self, heal_type):
        self.heals = list(heal_type)
        if self.heals[0] > 0:
            self.health += self.heals[1] * random.choice(multipliers)
            self.heals[0] -= 1
            return
        else:
            return 'nopp'

    def decrease_accuracy(self, n : float) -> None:
        self.accuracy -= n
        if self.accuracy < 0.25:
            self.accuracy = 0.25
    
    def rename(self, name):
        self.name = name
