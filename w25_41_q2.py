class Train():
    def __init__(self, trainIDNumber, route):
        self._trainIDNumber = trainIDNumber
        self._route = route
    
    def GetTrainIDNumber(self):
        return self._trainIDNumber

    def GetRoute(self):
        return self._route
    
class Station():
    def __init__(self, stationID, numberPlatforms):
        self._stationID = stationID
        self._numberPlatforms = numberPlatforms
        self._trains = []
        self._numberTrains = 0
    
    def AddTrain(self,train):
        if self._numberTrains >= self._numberPlatforms:
            return False
        else:
            self._trains.append(train)
            self._numberTrains += 1
            return True

    def GetTrains(self):
        if self._numberTrains == 0:
            return "There are no trains"
        else:
            print(f"The trains at station {self._stationID} are:")
            for train in self._trains:
                print(f"{train.GetTrainIDNumber()} on route number {train.GetRoute()}")

train1 = Train("12ADV", 134)
train2 = Train("33ART", 20)
train3 = Train("9FKF", 3)
train4 = Train("21VBC", 24)

station1 = Station("STH", 2)
station2 = Station("NTH", 1)

station1.AddTrain(train1)
station1.AddTrain(train2)
station1.AddTrain(train3)
station2.AddTrain(train4)

print(station1.GetTrains())
print(station2.GetTrains())