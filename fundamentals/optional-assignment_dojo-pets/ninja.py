from pet_class import Pet_Class

class Ninja:
    def __init__(self, first_name, last_name, treat, pet_food, pet_title = None):
        self.first_name = first_name
        self.last_name = last_name
        self.treat = treat
        self.pet_food = pet_food
        self.pet = pet_title

    def assign_pet(self, name, pet_type, trick, sound1, sound2, sound3):
        self.pet = Pet_Class(name, pet_type, trick, sound1, sound2, sound3)
        return self

    def walk(self):
        print(f"{self.first_name} gives {self.pet.pet_name} ({self.pet.pet_type}) a walk.")
        self.pet.affection_up_small()
        return self

    def feed(self):
        print(f'{self.first_name} feeds {self.pet.pet_name} ({self.pet.pet_type}) some {self.pet_food}.')
        self.pet.affection_up_small()
        return self

    def bathe(self):
        print(f'{self.first_name} gives {self.pet.pet_name} ({self.pet.pet_type}) a bath.')
        self.pet.noise3()
        return self

    def give_treat(self):
        print(f'{self.first_name} gives {self.pet.pet_name} ({self.pet.pet_type}) a {self.treat}')
        self.pet.noise3()
        print(f"{pet}\'s affection has grown!")
        self.pet.affection += 15
        return self


ninja_benji = Ninja('Benji', 'Hix', 'catpuccino', 'grilled salmon')

ninja_benji.assign_pet('Salad', 'cat', 'quad lutz', 'hmm', 'ゴゴゴゴゴゴゴ...', 'Oh... you\'re approaching me?')

ninja_benji.feed().walk().bathe()

ninja_benji.pet.do_trick()