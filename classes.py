import random
multipliers = [0.75, 0.8, 0.85, 0.95, 1, 1.05, 1.1, 1.15]


class Heal:
    def __init__(self, master, number=0):
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
            'punch': [5, 100, .9] # [damage, pp, accuracyindecimal(max=1)]
        }
        self.armour = [0.9, 100]
        self.heals = [5, 20]
        self.accuracy  = 1
        self.base_heal = Heal(self, 5)
        self.super_heal = SuperHeal(self, 0)
        self.full_heal = FullHeal(self)
    
    def level_up(self):
        self.level += 1
        self.exp = [0, self.exp[1]+20]

    # Going to use a randomiser to handle all combat stuff making it like a classic crpg.

    def take_damage(self, damage):
        self.health -= round(damage *(random.choice(multipliers)*self.armour[0]))
        self.armour[1] -= round(damage * (random.choice(multipliers)*(1-(self.armour[0]))))

    def attack(self, name):
        if name != 'defend':
            if self.attacks[name][1] > 0:
                self.attacks[name][1] -= 1
                accuracy = self.accuracy * self.attacks[name][2]* 100
                if random.randint(1, 100) <= accuracy:
                    return self.attacks[name] * random.choice(multipliers)
                else:
                    return 'missed'
            else:
                return 'nopp'
        else:
            if self.attacks[name][1] > 0:
                self.attacks[name][1] -= 1
                accuracy = self.accuracy * self.attacks[name][2] * 100
                if random.randint(1, 100) <= accuracy:
                    return 'nohealthloss'
                else:
                    return 'failed'

    def heal(self, heal_type):
        self.heals = list(heal_type)
        if self.heals[0] > 0:
            self.health += self.heals[1] * random.choice(multipliers)
            self.heals[0] -= 1
        else:
            return 'nopp'

    def decrease_accuracy(self, n : float) -> None:
        self.accuracy -= n
        if self.accuracy < 0.25:
            self.accuracy = 0.25
    
    def rename(self, name):
        self.name = name
    
    def buy_super_heal(self, amount):
        n = list(self.super_heal)[0] + amount
        self.super_heal = SuperHeal(self, n)

    def buy_heal(self, amount):
        n = list(self.heals)[0] + amount
        self.heals = Heal(self, n)
        
    def buy_full_heal(self, amount):
        n = list(self.full_heal)[0] + amount
        self.full_heal = FullHeal(self, n)

class Enemy(Parent):
    def __init__(self, name):
        super().__init__(name)
        self.attacks = {
            'slash' : [20, 30, .85],
            'defend' : [0, 5, .65],
            'revolver' : [40, 6, .35]
        }