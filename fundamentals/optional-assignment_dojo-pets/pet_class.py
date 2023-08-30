class Pet_Class:
    def __init__(self, pet_name, pet_type, trick, sound1, sound2, sound3):
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.trick = trick
        self.sound1 = sound1
        self.sound2 = sound2
        self.sound3 = sound3
        self.energy = 0
        self.health = 0
        self.affection = 0

    def sleep(self):
        self.energy += 25
        self.stats_up_small()
        return self

    def eat (self):
        self.energy += 5
        self.health += 10
        self.stats_up_small
        return self

    def play(self):
        self.health += 5
        self.stats_up_small()
        return self

    def affection_up_small(self):
        print(f'{self.pet_name} ({self.pet_type}) says: "{self.sound1}"')

    def stats_up_small(self):
        print(f'{self.pet_name} ({self.pet_type}) says: "{self.sound2}"')

    def noise3(self):
        print(f'{self.pet_name} ({self.pet_type}) says: "{self.sound3}"')
        return self

    def do_trick(self):
        print(f'{self.pet_name} ({self.pet_type}) does a {self.trick}')
        self.stats_up_small()
        self.affection += 5
        return self

    def display_stats(self):
        print(
        f"health: {self.health} \n",
        f"energy: {self.energy}"
        )
        return self

class Rock(Pet_Class):
    def __init__(self, pet_name, pet_type, trick, sound1, sound2, sound3):
        self.trick = 'nothing'
        self.sound1 = '...'
        self.sound2 = "."
        self.sound3 = "!"
    
    def do_trick(self):
        print(f'{self.pet_name} is a rock and therefore cannot do a trick')
        return self

    def play(self):
        print(f'{self.pet_name} is a rock and therefore cannot play')
        return self
        