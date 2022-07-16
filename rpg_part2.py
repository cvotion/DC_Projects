# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
from ast import Store
from curses import raw
from distutils.command import check
from random import random


from characters import *
from items import *


#todo maybe dead enemies can come back as zombies
 
#todo make reset method in character classes 

#todo call reset method while looping through list

 
    
def game():
    hero = Hero(10, 5, 30) 
    shadow = Shadow(1, 3, 3, 6)
    enemy_list.append(shadow)
    goblin = Goblin(6,2,1, 5)
    enemy_list.append(goblin)
    zombie = Zombie(1,4,2,1000)
    enemy_list.append(zombie)
    medic = Medic(6,2,1, 7)
    enemy_list.append(medic) 
    running = True
    
    
    
    # def print_enemies():
    #     for enemy in enemy_list:
    #         print(type(enemy).__name__)
    # print_enemies()
            
    def main_menu():
        print(f"""
            \n
            -----------------------
            What do you want to do?
            1. Go to store
            2. Heal
            3. Look for enemy
            4. Quit
            -----------------------
            """)
    def store_menu():
            print(f"""
            \n
            -----------------------
            What do you want to do?
            1. List items
            2. Buy item
            3. Collect bounty
            4. Exit shop
            -----------------------
            """)            
    def store():
        winston.greet()
        store_menu()
        raw_input = input()
        if raw_input == '1':
            winstons_store.print_items()
            print(""" \n
                  ### Winston ### 
                  Here's my current inventory!
                   """)
            print(f"Your Gold : {hero.gold}")
            store()
        elif raw_input == '2':
        # todo create item perks and impliment them into combat    
            winstons_store.print_items()
            print("""\n
                  ### Winston ### 
                  What caught your eye?
                   """)
            raw_input = (int(input()) - 1)
            if raw_input in range(len(winstons_store.store)):
                item = winstons_store.store[raw_input]
                
                print(f"""\n
                  ### Winston ### 
                  Ah, the {type(item).__name__}. That's a good one! That'll be {item.cost} gold.
                   """)
                if hero.gold >= item.cost:
                    hero.gold -= item.cost
                    hero.hero_items.append(item)
                    item.owner = hero
                    item.equip(hero)
                    print(f"{item.cost} has been deducted from your gold. You have {hero.gold} gold remaining.")
                    print(f"**{type(item).__name__} added to your items.**")
                else:
                    print(f"""\n
                  ### Winston ### 
                  It doesn't look like you have enough gold to buy the {type(item).__name__}. 
                  You need {item.cost - hero.gold} more gold for this item.
                  Try killing some enemies and collecting bounties to earn some money!
                   """)      
                store()  
            else:
                print("That's not a valid input")
                store()    
        elif raw_input == '3':
            winston.get_bounty(hero)
            store()
        elif raw_input == '4':
            winston.greet_counter = 0
            home()
        else:
            print("Sorry that's not a valid input!")
    def home():
        while running:
            main_menu()
            raw_input = input()
            if raw_input == '1':
                store()
            elif raw_input == '2':
                print("Resting for the night...")
                hero.health = 10
            elif raw_input == '3':
                print("Good luck!")
                fight()
            elif raw_input == '4':
                print("Good bye.")
                running == False
                quit()
            else:
                print("Sorry that's not a valid input!")
    def fight():
        enemy = Enemy.random_enemy()
        def fight_menu():
    # todo add inventory option during combat 

            print(f"""
                \n
                -----------------------
                What do you want to do?
                1. Attack {type(enemy).__name__}
                2. Use Item
                2. Switch Item
                2. do nothing
                3. flee
                -----------------------
                """)
        
        while enemy.alive() and hero.alive():
            # os.system('clear')
            hero.print_status()
            enemy.print_status()
            fight_menu()
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
                enemy = random.choice(enemy_list)        
                break
            
            
            else:
                print(f"Invalid input {raw_input}")
                
    home()            
        
        

game()

