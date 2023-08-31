from enemy import Enemy
from enemy import Rat
from enemy import Bandit
from enemy import Dragon
from player import Player
import random

answers = []

def skyrim_lite():
    player = Player()
    print('Welcome travlah!\nSit ye down and tell me about yeself! If a quest be yer aim, listen after... fate or fortune adventure awaits...\n')
    player.set_player_name(input('What shall I call ye?\n'))
    print(f"""Excellent {player.name}! 
    Now that we are a bit more accquainted, I can tell you about your quest.  

    Not much to it really! How brave are ye feelin?

    Ye can fight a squeeky innocent little Rat (AKA Benji), a carousing bloodthirsty Bandit (AKA Bryan), or the king of all predators (and hoarders), the Dragon (AKA Josh)!
    """)
    enemy = input('What will you choose?\n')
    if enemy == 'Rat':
        enemy = Rat()
    elif enemy == 'Bandit':
        enemy = Bandit()
    elif enemy == 'Dragon':
        enemy = Dragon()
    while player.health > 0 and enemy.enemy_health > 0:
        input('Press enter to Attack')
        player.player_attack(enemy)
        enemy.enemy_attack(player)
        player.display_stats().enemy_display_stats(enemy)

    if enemy.enemy_health <= 0:
        print("Victory!")
        print("""
        ⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⣠⠀⠀⢀⠀⠀⢠⠀⠀⠀
        ⠀⠀⢸⣧⠀⠀⠀⠀⢠⣾⣇⣀⣴⣿⠀⠀⣼⡇⠀⠀
        ⠀⠀⣾⣿⣧⠀⠀⢀⣼⣿⣿⣿⣿⣿⠀⣼⣿⣷⠀⠀
        ⠀⢸⣿⣿⣿⡀⠀⠸⠿⠿⣿⣿⣿⡟⢀⣿⣿⣿⡇⠀
        ⠀⣾⣿⣿⣿⣿⡀⠀⢀⣼⣿⣿⡿⠁⣿⣿⣿⣿⣷⠀
        ⢸⣿⣿⣿⣿⠁⣠⣤⣾⣿⣿⣯⣤⣄⠙⣿⣿⣿⣿⡇
        ⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿
        ⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏
        ⠀⠘⢿⣿⣿⣿⠛⠻⢿⣿⣿⣿⠹⠟⣿⣿⣿⣿⣿⠀
        ⠀⠀⠘⢿⣿⣿⣦⡄⢸⣿⣿⣿⡇⠠⣿⣿⣿⣿⡇⠀
        ⠀⠀⠀⠘⢿⣿⣿⠀⣸⣿⣿⣿⠇⠀⠙⣿⣿⣿⠁⠀
        ⠀⠀⠀⠀⠘⣿⠃⢰⣿⣿⣿⡇⠀⠀⠀⠈⢻⡇⠀⠀
        ⠀⠀⠀⠀⠀⠈⠀⠈⢿⣿⣿⣿⣶⡶⠂⠀⠀⠁⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡿⠋⠀⠀⠀
        """)
        input("Press enter to try again!\n")
        return True

    elif player.health <= 0:
        print(enemy.defeat)
        print('You are defeated! Bettah luck next time gov')
        input("Press enter to try again!\n")
        return True

isPlaying = True

while isPlaying == True:
    isPlaying = skyrim_lite()



