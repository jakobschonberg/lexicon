from random import randint
from time import sleep
from sys import exit
from world import World
from character import Character_Type
from bcolors import bcolors


def attack(relative_score, attacker_name, defender):
    sleep(2)
    roll = randint(1, 20) + relative_score
    damage = 0
    if roll <= 5: 
        print(f"{attacker_name} misses {defender.name}")
    elif roll <= 10:
        damage = randint(1, 3)
        print(f"{attacker_name} {bcolors.YELLOW}grazes{bcolors.END} {defender.name} for {damage} damage")
    else: #hit
        confirm_crit_roll = randint(1, 20) + relative_score
        if roll >= 20 and confirm_crit_roll >= 11:
            damage = randint(7, 10)
            print(f"{attacker_name} {bcolors.RED}critically hits{bcolors.END} {defender.name} for {damage} damage")
        else:
            damage = randint(4, 6)
            print(f"{attacker_name} {bcolors.ORANGE}hits{bcolors.END} {defender.name} for {damage} damage")
    defender.health -= damage


def do_combat() :
    print("combat starts")
    location = World.player.location
    player = World.player
    player_strength = player.combat_strength()
    enemies = []
    for character in location.characters:
        if character.character_type == Character_Type.enemy:
            enemies.append(character)
    while player.health > 0 and len(enemies):
        target_index = randint(0, len(enemies) - 1)
        target = enemies[target_index]
        attack(player_strength - target.combat_strength(), player.name, target)
        if target.health <= 0:
            del enemies[target_index]
            target.kill()
        for enemy in enemies:
            attack(enemy.combat_strength() - player_strength, enemy.name, player)
    if player.health <= 0:
        sleep(1)
        print(f"Game over - {bcolors.DARKRED}You have died{bcolors.END}.")
        sleep(2)
        exit(0)


