

#! Items

from characters import *


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
    def __init__(self, owner, cost):
        super(Item, self).__init__(owner)
        self.cost = cost   
            
class Armor(Item):
    pass

class Evade(Item):
    pass

class SuperTonic(Item):
    pass

winstons_store = Store("Winston")

armor = Armor("Winston", 25)
winstons_store.store.append(armor)
evade = Evade("Winston", 50)
winstons_store.store.append(evade)
supertonic = SuperTonic("Winston", 100)
winstons_store.store.append(supertonic)