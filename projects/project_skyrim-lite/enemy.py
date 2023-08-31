import random

class Enemy:

    def __init__(self, enemy_name, enemy_health, enemy_attack_stat):
        self.enemy_name = enemy_name
        self.enemy_health = enemy_health
        self.enemy_attack_stat = enemy_attack_stat
        self.enemy_roll = random.randrange(1, 10)

    def enemy_attack(self, player):
        enemy_damage = self.enemy_attack_stat + self.enemy_roll
        player.health -= enemy_damage
        print(f'{self.enemy_name} has done {enemy_damage} damage to {player.name}')
        return self

# ----------------------------- enemy subclasses ----------------------------- #
class Rat(Enemy):
    def __init__(self):
        self.enemy_name = 'Rat'
        self.enemy_health = 200000
        self.enemy_attack_stat = 1
        self.ouch = 'Benji says "uwu 👉👈"'
        self.defeat = 'Benji says "✨ur canceled😻"'


    def enemy_attack(self, player):
        enemy_roll = random.randrange(1, 10)
        enemy_damage = self.enemy_attack_stat + enemy_roll
        player.health -= enemy_damage
        print(f'{self.enemy_name} has done {enemy_damage} damage to {player.name}')
        return self

class Bandit(Enemy):
    def __init__(self):
        self.enemy_name = 'Bandit'
        self.enemy_health = 100
        self.enemy_attack_stat = 10
        self.ouch = 'Bryan says "OOF"'
        self.defeat = 'Bryan says "You shouldn\'t be here."'

    def enemy_attack(self, player):
        enemy_roll = random.randrange(1, 15)
        enemy_damage = self.enemy_attack_stat + enemy_roll
        player.health -= enemy_damage
        print(f'{self.enemy_name} has done {enemy_damage} damage to {player.name}')
        return self
        
class Dragon(Enemy):
    def __init__(self):
        self.enemy_name = 'Dragon'
        self.enemy_health = 110
        self.enemy_attack_stat = 14
        self.ouch = 'Josh says "foozrohdah"'
        self.defeat = 'Josh says "rawr 🦖"'

    def enemy_attack(self, player):
        enemy_roll = random.randrange(4, 15)
        enemy_damage = self.enemy_attack_stat + enemy_roll
        player.health -= enemy_damage
        print(f'{self.enemy_name} has done {enemy_damage} damage to {player.name}')
        return self
