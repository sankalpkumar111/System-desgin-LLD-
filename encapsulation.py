class SportBike:
    def __init__(self):
        self.__isStarted = False
        self.__currentSpeed = 0
        self.__currentGear = 0
        self._tyre_company = None  # For the property

    def start(self):
        self.__isStarted = True
        print("Sports Bike started")

    def stop(self):
        self.__isStarted = False
        self.__currentSpeed = 0
        self.__currentGear = 0
        print("Sports Bike stopped")

    @property
    def tyre_company(self):
        return self._tyre_company

    @tyre_company.setter
    def tyre_company(self, value):
        self._tyre_company = value

    def accelerate(self):
        if not self.__isStarted:
            print("Sports Bike is not started")
            return
        self.__currentSpeed += 10
        print(f"Accelerating... Current speed: {self.__currentSpeed} km/h")

    def brake(self):
        if not self.__isStarted:
            print("Sports Bike is not started")
            return
        self.__currentSpeed = max(0, self.__currentSpeed - 10)
        print(f"Braking... Current speed: {self.__currentSpeed} km/h")

    def changegear(self, gear: int):
        if not self.__isStarted:
            print("Sports Bike is not started")
            return
        self.__currentGear = gear
        print(f"Gear changed to {self.__currentGear}")


bike=SportBike()
bike.accelerate()
bike.start()
bike.accelerate()
bike.changegear(2)
bike.accelerate()
bike.brake()
bike.stop()
