

#! Items

from characters import *
#todo add armor as atribute to hero
#todo armor will have hp

class Store:
    def __init__(self, owner):
        self.owner = owner
    store = []
    def print_items(self):
        count = 1
        for item in self.store:
            cost = item.cost
            perk = item.perks
            item = type(item).__name__
            print(f"""\n
                  {count}. {item} : {cost} Gold
                  {perk}
                  """)
            count+=1

class Item(Store):
    def __init__(self, owner, cost, perks):
        super(Item, self).__init__(owner)
        self.cost = cost   
        self.perks = perks    

class Armor(Item):
    def __init__(self, owner, cost, perks, hp, defense):
        super().__init__(owner, cost, perks)
        self.hp = hp
        self.defense = defense
    def equip(self, hero):
        hero.armor_level = self.defense 
        hero.armor_hp = self.hp 

class Evade(Item):
    def __init__(self, owner, cost, perks, evade):
        super().__init__(owner, cost, perks)
        self.evade = evade
    def equip(self, hero):
        hero.evade_level += self.evade 
class SuperTonic(Item):
    def equip(self, hero):
        hero.health = 10
        print("Hero's health has been fully restored!")
        
class Zombie_killer(Item):
    def equip(self, hero):
        hero.zombie_killer = True       

winstons_store = Store("Winston")

armor = Armor("Winston", 15, "Defense +2", 15, 2)
winstons_store.store.append(armor)
evade = Evade("Winston", 20, """Evade +2 
            (chance of evading enemy attack increased by 2%)""", 2)
winstons_store.store.append(evade)
supertonic = SuperTonic("Winston", 30, """Fully restores hero health.
                    Can be used during battle.""")
winstons_store.store.append(supertonic)
zombie_kill = Zombie_killer("Winston", 200, """Magic rune equiped to your sword 
                        that will allow you to slay zombies.""")
winstons_store.store.append(zombie_kill)