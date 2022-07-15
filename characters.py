
#! Characters
import random
from typing import Type

from items import *


enemy_list = []
class Charater:
    def __init__(self, health, power, gold):
        self.health = health
        self.power = power
        self.gold = gold
        self.hit_counter = 0
        
        
    def alive(self):
        return self.health > 0
                 
    def print_status(self):
        print(f"The {type(self).__name__} has {self.health} health and {self.power} power.")
        
class NPC(Charater):

    def __init__(self, health, power, gold, name):
        super(NPC, self).__init__(health, power, gold)    
        self.name = name
        self.phrase = []
        self.greet_counter = 0
        
    def random_phrase(self):
        print(random.choice(self.phrase))
        
    def greet(self):
        if self.greet_counter < 1:
            print("""
                \n
        .------\ /------.
    |       -       |
    |               |
    |               |
    |               |
    _______________________
    ===========.===========
    / ~~~~~     ~~~~~ \
        
    /|     |     |      \
        
    W   ---  / \  ---   W
    
    \.      |o o|      ./
    |                 |
    \    #########    /
    \  ## ----- ##  /
        \##         ##/
        \_____v_____/
                """)
            print(f"""\n### {self.name} ###""")
            self.random_phrase()
            self.greet_counter += 1
        else:
            pass    
    def get_bounty(self, hero):
        total_bounty = 0
        count = 1
        for enemy in hero.enemies_killed:
            total_bounty += enemy.reward
            print(f"{count}. {type(enemy).__name__} : bounty -> {enemy.reward}")
            count += 1
        hero.gold += total_bounty  
        print(f"{total_bounty} gold has been added to your balance.")
        print(f"You now have {hero.gold} gold.")          
    
class Hero(Charater):
    
    hero_items = []
    enemies_killed = []
    # todo figure out how to do this as a dictionary maybe??
        
    def attack(self, enemy):
        if type(enemy).__name__ == 'Shadow' and enemy.gets_hit() == False:
            print("You strike the Shadow but nothing happens!")
            
        elif type(enemy).__name__ == 'Zombie':
            print("You attack the Zombie but it keeps coming toward you!") 
            enemy.attack(self)       
        else:  
            self.double_damage()  
            enemy.health -= self.power
            enemy.attack(self)
            print(f"You do {self.power} damage to the {type(enemy).__name__}.")
            self.power = 5
            if enemy.alive() == False:
                self.enemies_killed.append(enemy)
                print(f"The {type(enemy).__name__} is dead!")
                
    def double_damage(self):
        prob = random.randint(1, 10)
        if prob <= 2:
            self.power+= 2
            print("You made a critical hit!")
           
               
class Enemy(Charater):
    def __init__(self, health, power, gold, reward):
        super(Enemy, self).__init__(health, power, gold) 
        self.reward = reward
        
    def attack(self, hero):
        if type(Armor).__name__ in hero.hero_items:
                hero.health -= (self.power - type(Armor).__name__.item_bonus)
        else:        
            hero.health -= self.power
            print(f"The {type(self).__name__} does {self.power} damage to you.") 
    
    def add_enemy_to_list(self, name):
        enemy_list.append(name)  
        
    def random_enemy():
        enemy = random.choice(enemy_list) 
        return enemy      
    
class Goblin(Enemy):
    pass        
#todo os.system('clear')
class Medic(Enemy):
    
    def attack(self, hero):
        super().attack(hero)
        prob = random.randint(1, 10)
        if prob <= 2:
            self.health += 2
            print("The Medic has healed themselves!")

class Shadow(Enemy):
    def gets_hit(self):
        prob = random.randint(1, 10)
        if prob == 1:
            return True

class Zombie(Enemy):
    pass

class Wizard(Enemy):
    pass

class Demon(Enemy):
    pass

winston = NPC(5000,10000,25000,"Winston")
winston.phrase.append("Howdy! Take a look around my shop.")
winston.phrase.append("Welcome traveler, see anything you like?")
winston.phrase.append("I have plenty of magic items but don't ask me where I got them! ........ or else.")
winston.phrase.append("You wont find these items on Amazon! Suck it Bezos!")



