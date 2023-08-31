import random

class Player:
    def __init__(self):
        self.name = ''
        self.attack = 10
        self.health = 100


    def display_stats(self):
        print(f"Your remaining health is {self.health}")
        return self
    
    def enemy_display_stats(self, enemy):
        print(f"Your enemies remaining health is {enemy.enemy_health}")

    def player_attack(self, enemy):
        player_roll = random.randrange(10, 20)
        damage = self.attack + player_roll
        enemy.enemy_health -= damage
        print(f"{self.name} has done {damage} damage to {enemy.enemy_name}")
        print(enemy.ouch)
        return self
    
    def set_player_name(self, new_name):
        self.name = new_name
        print(f"Your new name is {self.name}")
        return self
