class Horse():
    def __init__(self, name, maxFenceHeight, percentageSuccess):
        self.__name = name
        self.__maxFenceHeight = maxFenceHeight
        self.__percentageSuccess = percentageSuccess
    
    def GetName(self):
        return self.__name
    
    def GetMaxFenceHeight(self):
        return self.__maxFenceHeight

    def Success(self, height, risk):
        if height > self.__maxFenceHeight:
            return 0.2 * self.__percentageSuccess
        else:
            match risk:
                case 1:
                    return self.__percentageSuccess
                case 2:
                    return self.__percentageSuccess * 0.9
                case 3:
                    return self.__percentageSuccess * 0.8
                case 4:
                    return self.__percentageSuccess * 0.7
                case 5:
                    return self.__percentageSuccess * 0.6

class Fence():
    def __init__(self, height, risk):
        self.__height = height
        self.__risk = risk
    
    def GetHeight(self):
        return self.__height
    
    def GetRisk(self):
        return self.__risk

Horses = [Horse("Beauty", 150, 72), Horse("Jet", 160, 65)]
Course = [None]*4

for i in range(len(Course)):
    valid = False
    while valid == False:
        height = int(input("input height: "))
        risk = int(input("input risk: "))

        if height >= 70 and height <= 180 and risk >= 1 and risk <= 5:
            valid = True
        else:
            print("invalid, try again")

    Course[i] = Fence(height, risk)

totalHorse1 = 0
totalHorse2 = 0

for i in range(len(Course)):
    Horse1Success = Horses[0].Success(Course[i].GetHeight(), Course[i].GetRisk())
    Horse2Success = Horses[1].Success(Course[i].GetHeight(), Course[i].GetRisk())

    totalHorse1 += Horse1Success
    totalHorse2 += Horse2Success

    print(f"{Horses[0].GetName()} has a {Horse1Success}% chance of success")
    print(f"{Horses[1].GetName()} has a {Horse2Success}% chance of success")
    print("")

avgHorse1 = totalHorse1 / 4
avgHorse2 = totalHorse2 / 4

if avgHorse1 > avgHorse2:
    print(f"{Horses[0].GetName()} has a {avgHorse1}% chance of jumping over all four fences")
else:
    print(f"{Horses[1].GetName()} has a {avgHorse2}% chance of jumping over all four fences")