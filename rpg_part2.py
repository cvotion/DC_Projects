# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
from random import random


enemy_list = []

#! Items

class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.store = []
    
    def add_item(self, name):
        name = Item(name)   
        self.store.append(name)
        
class Armor(Item):
    pass

class Evade(Item):
    pass

class SuperTonic(Item):
    pass

#! Characters
class Charater:
    def __init__(self, health, power, name, gold, reward):
        self.health = health
        self.power = power
        self.name = name
        self.gold = gold
        self.reward = reward
        self.hit_counter = 0
        
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            print(f"The {self.name} is dead.")
            return False
                 
    def print_status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")
        
    
           
        
class Hero(Charater):
        
    def attack(self, enemy):
        if enemy.name == 'Shadow' and enemy.hit_counter < 9:
            enemy.hit_counter += 1
            print("You strike the Shadow but nothing happens!")
            if enemy.hit_counter == 5:
                enemy.attack(self)
        else:    
            enemy.health -= self.power
            enemy.hit_counter = 0
            print(f"You do {self.power} damage to the {enemy.name}.")
               
    
    
class Goblin(Charater):
    
    def attack(self, hero):
        hero.health -= self.power
        print(f"The {self.name} does {self.power} damage to you.")        

class Medic(Charater):
    pass

class Shadow(Charater):
    def attack(self, hero):
        hero.health -= self.power
        print(f"The {self.name} does {self.power} damage to you.") 
    

class Zombie(Charater):
    pass

class Wizard(Charater):
    pass

class Demon(Charater):
    pass 


   
    
def main():
    hero = Hero(10, 5, 'Hero', 10, 0)        
    Shadow.create_enemy(1, 3, 'Shadow', 0, 6)
    Goblin.create_enemy(6,2,'Goblin',1, 5)
    enemy = random.choice(enemy_list)

    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks enemy
            hero.attack(enemy)
            
        elif raw_input == "2":
            if enemy.alive:
            # enemy attacks hero
                enemy.attack(hero)
            
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        

main()

