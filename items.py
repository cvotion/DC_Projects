

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
            item = type(item).__name__
            print(f"""\n
                  {count}. {item} : {cost} Gold""")
            count+=1

class Item(Store):
    def __init__(self, owner, cost, perks):
        super(Item, self).__init__(owner)
        self.cost = cost   
        self.perks = perks    

class Armor(Item):
    def __init__(self, owner, cost, perks, hp, item_bonus):
        super().__init__(owner, cost, perks)
        self.hp = hp
        self.item_bonus = item_bonus
        

class Evade(Item):
    pass

class SuperTonic(Item):
    pass

winstons_store = Store("Winston")

armor = Armor("Winston", 25, "Defense +2", 15, 2)
winstons_store.store.append(armor)
evade = Evade("Winston", 50, "perk")
winstons_store.store.append(evade)
supertonic = SuperTonic("Winston", 100, "perk")
winstons_store.store.append(supertonic)