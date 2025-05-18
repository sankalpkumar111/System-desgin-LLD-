class Car:
    def __init__(self):
        self._isStarted=False
        self._currentSpeed=0
        self._currentGear=0
    
    def start(self):
        self._isStarted=True
        print("Car started")
    
    def stop(self):
        self._isStarted=False
        self._currentSpeed=0
        print("Car stopped")
    
    def accelrate(self):
        if not self._isStarted:
            print("Car is not started")
            return
        
        self._currentSpeed=self._currentSpeed+20
        print(f"Accelerating... Current speed: {self._currentSpeed} km/h")
    
    def brake(self):
        if not self._isStarted:
            print("Car is not started")
            return
        self._currentSpeed=self._currentSpeed-20
        print(f"Braking... Current speed: {self._currentSpeed} km/h")
    

class ManualCar(Car):
    __CURRENT_GEAR=0
    
    def __init__(self,brand,model):
        super().__init__()
        self._brand=brand
        self._model=model
    
    def shiftgear(self,gear:int):
        self.__CURRENT_GEAR=gear
        print(f"{self._brand}  {self._model} Gear changed to {self.__CURRENT_GEAR}")
    

class ElectricCar(Car):
    __battery_Level=0
    def __init__(self,brand,model):
        super().__init__()
        self._brand=brand
        self._model=model
    
    def charge_battery(self):
        self.__battery_Level=100
        print(f"{self._brand}  {self._model} Battery charged to {self.__battery_Level}%")

man_car=ManualCar("Honda","Civic")
man_car.start()
man_car.accelrate()
man_car.brake()
man_car.shiftgear(2)
man_car.stop()

print("------------------------------------------------------------------------")

ele_car=ElectricCar("Tesla","Model 3")
ele_car.start()
ele_car.accelrate()
ele_car.brake()
ele_car.charge_battery()
ele_car.stop()
        