# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Charater:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            print(f"The {self.name} is dead.")
            return False
            
            
    def print_status(self):
        print(f"The {self.name} has {self.health} health and {self.power} power.")
        
class Hero(Charater):
        
    def attack(self, goblin):
        goblin.health -= self.power
        print(f"You do {self.power} damage to the goblin.")
           
class Goblin(Charater):
    
    def attack(self, hero):
        hero.health -= self.power
        print(f"The goblin does {self.power} damage to you.")
                
    
    
def main():
    hero = Hero(10, 5, 'Hero')        
    goblin = Goblin(6, 2, 'Goblin')

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            
        elif raw_input == "2":
            if goblin.alive:
            # Goblin attacks hero
                goblin.attack(hero)
            
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        

main()

