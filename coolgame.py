import random
import time
import datetime
from datetime import datetime

class EventItem():
    def __init__(self, eventName, type, difficulty, winText, loseText, drawText):
        self.__eventName = eventName  #STRING
        self.__type = type  #STRING
        self.__difficulty = difficulty #INTEGER
        self.__winText = winText
        self.__loseText = loseText
        self.__drawText = drawText
    
    def GetName(self):
        return self.__eventName

    def GetDifficulty(self):
        return self.__difficulty
    
    def GetEventType(self):
        return self.__type
    
    def GetWinText(self):
        return self.__winText
    
    def GetLoseText(self):
        return self.__loseText
    
    def GetDrawText(self):
        return self.__drawText

class Character():
    def __init__(self, characterName, Strength, Stamina, Endurance, Intelligence):
        self.__characterName = characterName  #STRING
        self.__Strength = Strength  #INTEGER
        self.__Stamina = Stamina  #INTEGER
        self.__Endurance = Endurance  #INTEGER
        self.__Intelligence = Intelligence  #INTEGER
    
    def GetName(self):
        return self.__characterName
    
    def GetStrength(self):
        return self.__Strength

    def GetStamina(self):
        return self.__Stamina
    
    def GetEndurance(self):
        return self.__Endurance

    def GetIntelligence(self):
        return self.__Intelligence

    def AddStrength(self, amount):
        self.__Strength += amount
        if Player == self:
            if amount > 0:
                PrintLine(f"(+{amount} Strength)",1)
            else:
                PrintLine(f"({amount} Strength)",1)

    def AddStamina(self, amount):
        self.__Stamina += amount
        if Player == self:
            if amount > 0:
                PrintLine(f"(+{amount} Stamina)",1)
            else:
                PrintLine(f"({amount} Stamina)",1)
    
    def AddEndurance(self, amount):
        self.__Endurance += amount
        if Player == self:
            if amount > 0:
                PrintLine(f"(+{amount} Endurance)",1)
            else:
                PrintLine(f"({amount} Endurance)",1)

    def AddIntelligence(self, amount):
        self.__Intelligence += amount
        if Player == self:
            if amount > 0:
                PrintLine(f"(+{amount} Intelligence)",1)
            else:
                PrintLine(f"({amount} Intelligence)",1)
        
    def CalculateScore(self, eventType, difficulty):
        match eventType:
            case "Strength":
                    difference = difficulty - self.__Strength
            case "Stamina":
                    difference = difficulty - self.__Stamina
            case "Endurance":
                    difference = difficulty - self.__Endurance
            case "Intelligence":
                    difference = difficulty - self.__Intelligence
        
        return self.__CalculateChance(difference)
    
    def __CalculateChance(self, difference):
        if difference <= 0:         
            return 100
        if difference >= 11:         
            return random.randint(0, 3)
        
        chancesTable = {
            1:(80,90), 2:(70,80), 3:(60,70), 4:(50,60), 5:(40,50),
            6:(30,40), 7:(20,30), 8:(10,20), 9:(0,10), 10:(0,5)
        }
   
        low, high = chancesTable[difference]
        return random.randint(low, high)

        
def PrintLine(text, speed, End="\n"):
    for i in range(len(text)):
        if i < len(text) - 1:
            print(text[i], end="")
        else:
            print(text[i], end=End)
        time.sleep(0.05/speed)

def answer(prompt, valid):
    while True:
        try:
            value = int(input(prompt))
            if value in valid: return value
        except ValueError:
            pass
        print("Please type a valid number:", valid)

CharacterList= [
    Character("Stepan The Slayer", 4, 6, 3, 3),
    Character("Berta The Beast", 1, 2, 4, 10),
    Character("Baris The Butcher", 99999, 99999, 99999, 99999),
    Character("Dragos The Dragon", 7, 0, 1, 6),
    Character("Noah The Noob", 6, 2, 0, 7),
    Character("Daniel The Demon", 2, 4, 8, 0)
]
EventsList = [
    EventItem("Arm Wrestling", "Strength", 6, f" wins the match!", f" Got their arm shattered", f"They arm-wrestle 6 hours straight until they both get too tired and faint - its a draw"),
    EventItem("100m Sprint", "Stamina", 3, f" Gets to the finish line first!", f" Trips and faceplants the floor", f"They both get to the finish line at exacly the same time - its a draw"),
    EventItem("Boxing Match", "Endurance", 4, f" Performs a powerful punch to the head and wins!", f" Gets permament brain damage", f"They were too scared to fight each other - Its a draw"),
    EventItem("Game of Chess", "Intelligence", 8, f" Checkmates and wins!", f" Gets angry and flips the chess board", f"Its a stalemate!"),
    EventItem("Pushups Competition", "Strength", 7, f" Wins by doing {random.randint(15,50)} pushups!", f" faints from doing so many pushups", f"They both do the same amount of push-ups - its a draw"),
    EventItem("Ice Bath Challenge", "Endurance", 5, f" stays in the freezing water like a champ!", f" jumps out screaming after 3 seconds", f"they both shiver uncontrollably — it’s a draw"),
    EventItem("Math Exam", "Intelligence", 8, f" solves every problem with ease!", f" writes their name wrong", f"they both score the same — it’s a draw"),
    EventItem("Cycling Race", "Stamina", 4, f" pedals past the finish line!", f" crashes into a bush", f"they both run out of energy — it’s a draw"),
    EventItem("Swim Across the Lake", "Stamina", 6, f" reaches the shore!", f" sinks halfway and has to be rescued", f"they meet in the middle and agree to stop — it’s a draw"),
    EventItem("Tree-Chopping Challenge", "Strength", 5, f" chops down the tree in seconds!", f" loses grip and cuts off their finger", f"they both give up halfway — it’s a draw"),
    EventItem("Tug-of-War", "Strength", 7, f" pulls the opponent straight into the ground!", f" gets yanked into the dirt face-first", f"the rope snaps — no one wins"),
    EventItem("10 kilometer race", "Endurance", 7, f" Makes it to the finish line just under {random.randint(40,55)} minutes!", f" Faints half-way through the race!", f"Neither of them made it to the finish line - It's a draw"),
    EventItem("Eating contest", "Endurance", 3, f" Inhales all the hot-dogs in a matter of minutes!", f" Throws up after eating 3 hotdogs", f"Neither of them managed to eat all of the hotdogs - It's a draw"),

]

Questions = [
    {
        "question": "You’re a toddler playing in the playground. What are you doing?",
        "options": [
            "1. Lifting heavy toys", 
            "2. Chasing other kids",
            "3. Eating dirt",  
            "4. Staring at ants and wonder what they're planning"  
        ]
    },
    {
        "question": "You’re now in kindergarden and it's playtime! You...",
        "options": [
            "1. Wrestle with the other kids", 
            "2. Run around the room",
            "3. Attempt to do the splits",  
            "4. Try to solve the hardest puzzle that they have"  
        ]
    },
    {
        "question": "You're parents want to enroll you in an after-school activity, you choose to...",
        "options": [
            "1. Join the wrestling club", 
            "2. Join the athletics club",
            "3. Join the hiking and camping club",  
            "4. Join the reading club",
        ]
    },
    {
        "question": "You are being bullied by an older kid, You...",
        "options": [
            "1. Punch him in the face", 
            "2. Outrun him",
            "3. Choose to ignore him",  
            "4. Outsmart him with a clever prank" 
        ]
    },
    {
        "question": "You are now starting your A-Levels, Your favourite subject is...",
        "options": [
            "1. P.E", 
            "2. Computer Science",  
            "3. Physics",
            "4. Further Maths"
        ]
    },
    {
        "question": "What do you do in your free time?",
        "options": [
            "1. Go to the gym", 
            "2. Go for a run",
            "3. Go for long hikes in the mountains",  
            "4. Study for school" 
        ]
    },
        {
        "question": "You've finished school! What do you do now? ",
        "options": [
            "1. Become a MMA fighter", 
            "2. Become a professional athlete",
            "3. Become a firefighter",  
            "4. Go to university" 
        ]
    },
    
]

GenderQuestion = {
        "question": "Select your gender",
        "options": [
            "1. Male", 
            "2. Female",
        ]
}

TournamentQuestion = {
        "question": "What do you choose to do after the Tournament?",
        "options": [
            "1. Go train at the gym", 
            "2. Go for a run",
            "3. Go camping in the mountains",  
            "4. Read a book",
            "5. Retire",
        ]
}


PlrName = str(input("Input Your Desired Name: "))
Player = Character(PlrName, 0,0,0,0)


PrintLine(f"{GenderQuestion['question']}\n", 1.5)
for Option in GenderQuestion['options']:
    PrintLine(f"{Option}", 2.5)

Answer = answer("Enter your answer: ", range(1, len(GenderQuestion['options'])+1))
Gender = ""
match Answer:
    case 1:
        Gender = "Male"
        Player.AddStrength(2)
    case 2:
        Gender = "Female"
        Player.AddEndurance(2)

print("")

PrintLine(f"Name: {PlrName}, Gender: {Gender}", 0.35)
time.sleep(1)
PrintLine(f"Date Of Birth: {datetime.today().strftime('%d/%m/%Y')}", 0.5)
time.sleep(0.5)
PrintLine(f"Time Of Birth: {datetime.today().strftime('%H:%M:%S')}", 0.5)
time.sleep(0.5)

print("")

PrintLine(f"Age 0", 0.35)
time.sleep(0.5)
PrintLine(f"You have entered the world, small, but mighty", 1)
PrintLine(f"Ready to face whatever life throws at you", 1)
time.sleep(3)
print("")

for i in range(len(Questions)):
    match i:
        case 0:
            PrintLine(f"Age 2", 0.35)
            time.sleep(0.5)
        case 1:
            PrintLine(f"Age 3", 0.35)
            time.sleep(0.5)
        case 2:
            PrintLine(f"Age 5", 0.35)
            time.sleep(0.5)
            PrintLine(f"A big day has come, Your first day of school!", 1)
            time.sleep(0.1)
            PrintLine(f"You're nervous but exited at the same time", 1)
            time.sleep(1)
            print()
            PrintLine(f"Age 7", 0.35)
            time.sleep(0.5)
            PrintLine(f"School has been going really well, you've even made a couple of close friends!", 1)
            time.sleep(1)
        case 4:
            PrintLine(f"Age 16", 0.35)
            print("")
            time.sleep(0.5)
        case 6:
            PrintLine(f"Age 18", 0.35)
            print("")
            time.sleep(0.5)

    PrintLine(f"{Questions[i]['question']}\n", 1.5)
    for Option in Questions[i]['options']:
        PrintLine(f"{Option}", 2.5)

    Answer = answer("Enter your answer: ", range(1, len(Questions[i]['options'])+1))
    match Answer:
        case 1:
            Player.AddStrength(2)
        case 2:
            Player.AddStamina(2)
        case 3:
            Player.AddEndurance(2)
        case 4:
            Player.AddIntelligence(2)

    print("")

time.sleep(2)
PrintLine(f"Age 22", 0.35)
time.sleep(0.5)
PrintLine(f"So far, you've been living a simple, but happy life", 1)
time.sleep(0.5)
PrintLine(f"But soon that's going to change...", 0.65)
time.sleep(2)
PrintLine(f"It is a regular day, you just got off work", 1)
time.sleep(0.5)
PrintLine(f"A mysterious woman in a suit approaches you", 1)
time.sleep(0.5)
PrintLine(f"She has been watching you for a while now and is impressed with the skills you have achieved", 1)
time.sleep(2)
PrintLine(f"She makes you an offer that you can't resist", 1)
time.sleep(1)
PrintLine(f"'Fight in the Tournament, for a chance to win the grand prize of 10 million euros'", 1)
time.sleep(2)
PrintLine(f"Next thing you know, you are about to enter your first battle", 1)
time.sleep(4)
print("")
print("")

TotalWins = 0
TotalLose = 0
TotalDraws = 0
TotalEarnings = 0


while True:
    Opponent = random.choice(CharacterList)

    PrintLine(f"You: {Player.GetName()} | Strength: {Player.GetStrength()} | Stamina: {Player.GetStamina()} | Endurance: {Player.GetEndurance()} | Intelligence: {Player.GetIntelligence()}",1.5)
    print("")
    time.sleep(5)
    PrintLine(f"Are up against...", 0.75)
    time.sleep(1)
    print("")
    PrintLine(f"Opponent: {Opponent.GetName()} | Strength: {Opponent.GetStrength()} | Stamina: {Opponent.GetStamina()} | Endurance: {Opponent.GetEndurance()} | Intelligence: {Opponent.GetIntelligence()}",1.5)
    time.sleep(3.5)
    print("")
    print("")

    PrintLine(f"Let the games begin!", 0.75)
    print("")
    time.sleep(1)

    PlayerPoints = 0
    OpponentPoints = 0
    EventsPlayed = []

    for i in range(5):
        repeatedEvent = True
        while repeatedEvent:
            repeatedEvent = False
            Event = random.choice(EventsList)
            for event in EventsPlayed:
                if Event == event:
                    repeatedEvent = True
        
        EventsPlayed.append(Event)

        PrintLine(f"Round {i+1} | Event: {Event.GetName()}",1.25)
        print("")

        time.sleep(4)

        PlayerChance = Player.CalculateScore(Event.GetEventType(), Event.GetDifficulty())
        OpponentChance = Opponent.CalculateScore(Event.GetEventType(), Event.GetDifficulty())

        if PlayerChance == OpponentChance:
            PrintLine(Event.GetDrawText(),1)
        elif PlayerChance > OpponentChance:
            PlayerPoints += 1
            PrintLine(f"{Player.GetName()}{Event.GetWinText()}",1)
            time.sleep(3)
            PrintLine(f"{Opponent.GetName()}{Event.GetLoseText()}",1)
        else:
            OpponentPoints += 1
            PrintLine(f"{Opponent.GetName()}{Event.GetWinText()}",1)
            time.sleep(3)
            PrintLine(f"{Player.GetName()}{Event.GetLoseText()}",1)
        
        print("")
        print("")
        time.sleep(6)

    if PlayerPoints == OpponentPoints:
        TotalDraws += 1
        PrintLine("It is a draw!",1)
        time.sleep(1)
        PrintLine("You both get to split the prize and get 5 million euros each!",1)
        time.sleep(3)
    elif PlayerPoints > OpponentPoints:
        TotalWins += 1
        PrintLine(f"{Player.GetName()} won with {PlayerPoints} points!",1)
        time.sleep(1)
        PrintLine("Congratulations! You have won the grand prize of 10 Million Euros!",1)
        time.sleep(3)
    else:
        TotalLose += 1
        PrintLine(f"{Opponent.GetName()} won with {OpponentPoints} points",1)
        PrintLine("You lost, That's quite unfortunate :(",1)
        PrintLine("But don't worry, it's not over yet...",1)
        time.sleep(3)

    print("")

    PrintLine(f"{TournamentQuestion['question']}\n", 1.5)
    for Option in TournamentQuestion['options']:
        PrintLine(f"{Option}", 2.5)

    Answer = answer("Enter your answer: ", range(1, len(Questions[i]['options'])+1))
    match Answer:
        case 1:
            Player.AddStrength(2)
        case 2:
            Player.AddStamina(2)
        case 3:
            Player.AddEndurance(2)
        case 4:
            Player.AddIntelligence(2)
        case 5:
            print("")
            PrintLine(f"You successfully retired with {TotalWins} Total Wins, {TotalLose} Total Losses, {TotalDraws} Total Draws, and have earned {(TotalWins * 10) + (TotalDraws * 5)} Million euros in prize money!",1)
            break
    
    for character in CharacterList:
        if character.GetName() != "Baris The Butcher":
            RandomStat = random.randint(1,4)

            match RandomStat:
                case 1:
                    character.AddStrength(1)
                case 2:
                    character.AddStamina(1)
                case 3:
                    character.AddEndurance(1)
                case 4:
                    character.AddIntelligence(1)
    print("")
