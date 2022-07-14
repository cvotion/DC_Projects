class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    def attack(self, goblin):
        goblin.health -= self.power
        print(f"You do {self.power} damage to the goblin.")
        if goblin.health <= 0:
            print("The goblin is dead.")        
    def alive(self):
        if self.health != 0:
            return True         
    
class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, hero):
        hero.health -= self.power
        print("The goblin does {self.power} damage to you.")
        if hero.health <= 0:
            print("You are dead.")        
    def alive(self):
        if self.health != 0:
            return True  
        
          
hero = Hero(10, 5)        
goblin = Goblin(6, 2)        
