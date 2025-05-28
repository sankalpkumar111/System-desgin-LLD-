from abc import ABC ,abstractmethod

class Singleton:
    isinstance=False
    
    def __init__(self):
        print("Singleton Constructor created")
    
    def __new__(cls):
        if not cls.isinstance:
            cls.isinstance=True
            return super().__new__(cls)
        else:
            return None


obj1=Singleton()
obj2=Singleton()

print(obj1!=obj2)