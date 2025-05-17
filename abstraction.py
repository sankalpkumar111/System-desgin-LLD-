from abc import ABC ,abstractmethod
class Bike(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def brake(self):
        pass
    
    @abstractmethod
    def changegear(self,gear:int):
        pass


class SportsBike(Bike):
    def __init__(self):
        self.isStarted=False
        self.currentSpeed=0
        self.currentGear=0
    def start(self):
        """
        Starts the sports bike

        Sets isStarted to True and prints a success message
        """
        self.isStarted=True
        print("Sports Bike started")
    
    def stop(self):
        self.isStarted=False
        self.gear=0
        self.accelrate=0
        print("Sports Bike stopped")

    def accelerate(self):
        if not self.isStarted:
            print("Sports Bike is not started")
            return
            
        
        self.currentSpeed=self.currentSpeed+10
        print(f"Accelerating... Current speed: {self.currentSpeed} km/h")
        
    def changegear(self,gear:int):
        if not self.isStarted:
            print("Sports Bike is not started")
            return
        
        self.currentGear=gear
        print(f"Gear changed to {self.currentGear}")
    
    def brake(self):
        if not self.isStarted:
            print("Sports Bike is not started")
            return
        self.currentSpeed=self.currentSpeed-10
        print(f"Braking... Current speed: {self.currentSpeed} km/h")
        
bike=SportsBike()
bike.accelerate()
bike.start()
bike.accelerate()
bike.changegear(2)
bike.accelerate()
bike.brake()
bike.stop()

    
