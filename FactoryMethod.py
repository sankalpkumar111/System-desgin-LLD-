from abc import ABC,abstractmethod
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

class BasicBurger(Burger):
    def prepare(self):
        print("Making a Basic burger for customer")

class StabardBurger(Burger):
    def prepare(self):
        print("Making a Standard Burger for customer")

class PremiumBurger(Burger):
    def prepare(self):
        print("Making a Premium Burger for customer")

class BasicWheatBurger(Burger):
    def prepare(self):
        print("Making a Basic Wheat burger for customer")

class StandardWheatBurger(Burger):
    def prepare(self):
        print("Making a Standard Wheat Burger for customer")

class PremiumWheatBurger(Burger):
    def prepare(self):
        print("Making a Premium Wheat Burger for customer")
    
class BurgerFactory(ABC):
    @abstractmethod
    def createburger(self,type:str)->Burger:
        pass
    
class SinghBurger(BurgerFactory):
    def createburger(self, type:str)-> Burger:
        type=type.lower()
        
        if type=="basic":
            return BasicBurger()
        elif type=="standard":
            return StabardBurger()
        elif type=="premium":
            return PremiumBurger()
        else:
            return None

class KingBurger(BurgerFactory):
    def createburger(self, type:str)-> Burger:
        type=type.lower()
        
        if type=="basic":
            return BasicWheatBurger()
        elif type=="standard":
            return StandardWheatBurger()
        elif type=="premium":
            return PremiumWheatBurger()
        else:
            return None

print("Choose Burger Brand:\n1. SinghBurger\n2. KingBurger")
brand_choice = input("Enter choice (1 or 2): ")

if brand_choice == "1":
    obj = SinghBurger()
elif brand_choice == "2":
    obj = KingBurger()
else:
    print("Invalid choice.")
    exit()

print("Burger types available:\nBasic\nStandard\nPremium")
burger_type = input("Enter a Burger type: ")

burger = obj.createburger(burger_type)
if burger:
    burger.prepare()
else:
    print("Invalid burger type.")
