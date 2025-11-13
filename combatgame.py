import random
import time
from rich.console import Console

class Character():
    def __init__(self, name, attackName, powermoveName, maxhp=50, atk=4, guard_dmg_reduction=1, dodgeChance=0.05, critChance=0.05):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.atk = atk
        self.attackName = attackName
        self.powermoveName = powermoveName
        self.guard_dmg_reduction = guard_dmg_reduction
        self.dodgeChance = dodgeChance
        self.critChance = critChance
        self.energy = 0 
    
    def new_round(self):
        self.guard_dmg_reduction = 1
        self.energy += 1

    def attack(self, target, powerMove=False):
        damage = round(random.uniform(0.5,1.5),1) * self.atk

        critChance = random.randint(0,100)
        dodgeChance = random.randint(0,100)
        crit = False
        dodge = False

        if critChance/100 <= self.critChance:
            crit = True
            damage *= 2
        if dodgeChance <= target.dodgeChance:
            dodge = True
            damage = 0
        if powerMove:
            damage *= 2

        target.hp -= min(max(0, damage * target.guard_dmg_reduction), target.hp)

        if dodge:
            PrintLine(f"[bold]{target.name}[/] [bold][green]dodges!", 1)
        else:
            if powerMove:
                if crit:
                    PrintLine(f"[bold]{self.name}[/] performs a [bold][bright_yellow]CRITICAL [blue]{self.powermoveName}[/] to [bold]{target.name}!", 1)
                else:
                    PrintLine(f"[bold]{self.name}[/] performs a [bold][blue]{self.powermoveName}[/] to [bold]{target.name}!", 1)
            else: 
                if crit:
                    PrintLine(f"[bold]{self.name}[/] performs a [bold][bright_yellow]CRITICAL [blue]{self.attackName}[/] to [bold]{target.name}!", 1)
                else:
                    PrintLine(f"[bold]{self.name}[/] performs a [bold][blue]{self.attackName}[/] to [bold]{target.name}!", 1)
                
            if not dodge:
                time.sleep(1.5)
                PrintLine(f"[bold]{target.name}'s[/] health is now at [bold][red]{round(target.hp, 1)}", 1)
    
    def guard(self):
        self.guard_dmg_reduction = 0.6
        PrintLine(f"[bold]{self.name}[/] [blue]guards[/]!", 1)
        time.sleep(1.5)
        PrintLine(f"[bold]{self.name}'s[/] defence is now at [bold][blue]{round((1-self.guard_dmg_reduction)*100, 1)}%", 1)

def PrintLine(text, speed):
    currentStyle = ""
    loadingStyle = False
    for i in range(len(text)):
        if loadingStyle:
            currentStyle = currentStyle + text[i]
            if text[i] == "]":
                if text[i-1] == "/":
                    currentStyle = ""
                loadingStyle = False
        else:
            if text[i] == "[":
                loadingStyle = True
                currentStyle = currentStyle + text[i]
            else:
                if i < len(text) - 1:
                    Console().print(currentStyle+text[i], end="")
                else:   
                    Console().print(currentStyle+text[i], end="\n")
                time.sleep(0.05/speed)

def move(prompt, valid):
    while True:
        try:
            value = int(Console().input(prompt))
            if value in valid: return value
        except ValueError:
            pass
        print("Please type a valid number:", valid)

Player = Character("Player", "Punch", "Tornado Kick", maxhp=50, atk=4, guard_dmg_reduction=1, dodgeChance=0.3, critChance=0.15)
Bear = Character("Bear", "Bite", "Maul", maxhp=40, atk=5.5, guard_dmg_reduction=1, dodgeChance=0.05, critChance=0.4)

def fight(Enemy):
    while True:
        PrintLine(f"[bold]{Player.name}[/] | Health: [bold][red]{round(Player.hp, 1)}[/] | Attack: {Player.atk} | Energy: {Player.energy} | Defence [bold][blue]{(1-Player.guard_dmg_reduction)*100}%", 2)
        PrintLine(f"[bold]{Enemy.name}[/] | Health: [bold][red]{round(Enemy.hp, 1)}[/] | Attack: {Enemy.atk} | Energy: {Enemy.energy} | Defence [bold][blue]{(1-Enemy.guard_dmg_reduction)*100}%", 2)

        time.sleep(0.5)
        print("")

        while True:
            Move = move(f"[underline]Choose your move:[/] \n1. {Player.attackName}\n2. {Player.powermoveName} \n3. Guard \n", range(1,4))
            if Move == 2 and Player.energy < 2:
                continue
            else:
                break

        match Move:
            case 1:
                Player.attack(Enemy)
                time.sleep(3)
            case 2:
                Player.attack(Enemy, powerMove=True)
                time.sleep(3)
            case 3:
                Player.guard()
                time.sleep(3)
        
        print("")

        if Player.hp == 0:
            print("You died!")
            break

        if Enemy.hp == 0:
            PrintLine(f"{Enemy.name} dies!", 1)
            break


        if Enemy.energy < 2:
            if Enemy.hp / Enemy.maxhp < 0.5:
                Enemy.guard()
                time.sleep(3)
            else:
                Enemy.attack(Player)
                time.sleep(3)
        else:
            roll = random.randint(1,10)
            if roll <= 7:
                Enemy.attack(Player, powerMove=True)
                time.sleep(3)
            else:
                Enemy.attack(Player)
                time.sleep(3)
        
        if Player.hp == 0:
            print("You died!")
            break

        if Enemy.hp == 0:
            PrintLine(f"{Enemy.name} dies!", 1)
            break
        
        Player.new_round()
        Enemy.new_round()
        print("")

fight(Bear)