class Vehicle():
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__ID = ID
        self.__MaxSpeed = MaxSpeed
        self.__CurrentSpeed = 0 
        self.__IncreaseAmount = IncreaseAmount
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
        
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def SetCurrentSpeed(self, speed):
        self.__CurrentSpeed = speed
    
    def SetHorizontalPosition(self, pos):
        self.__HorizontalPosition = pos

    def IncreaseSpeed(self):
        NewSpeed = self.GetCurrentSpeed() + self.GetIncreaseAmount()
        if NewSpeed > self.GetMaxSpeed():
            NewSpeed = self.GetMaxSpeed()
       
        self.SetCurrentSpeed(NewSpeed)
        self.SetHorizontalPosition(self.GetHorizontalPosition() + self.GetCurrentSpeed())

    def outputSpeedAndPos(self):
        print(f"horizontal position: {self.GetHorizontalPosition()}")
        print(f"speed: {self.GetCurrentSpeed()}")

class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalChange
        self.__MaxHeight = MaxHeight
    
    def GetVerticalPosition(self):
        return self.__VerticalPosition
    
    def IncreaseSpeed(self):
        super().IncreaseSpeed()
        
        NewPos = self.__VerticalPosition + self.__VerticalChange
        if NewPos > self.__MaxHeight:
            NewPos = self.__MaxHeight

        self.__VerticalPosition = NewPos

    def outputSpeedAndPos(self):
        super().outputSpeedAndPos()
        print(f"vertical position: {self.GetVerticalPosition()}")

Car = Vehicle("Tiger", 100, 20)
Heli = Helicopter("Lion", 350, 40, 3, 100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.outputSpeedAndPos()

Heli.IncreaseSpeed()
Heli.IncreaseSpeed()
Heli.outputSpeedAndPos()