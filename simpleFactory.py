from abc import ABC, abstractmethod
class Burger(ABC):
        @abstractmethod
        def prepare(self):
                pass
class BasicBurger(Burger):
        def prepare(self):
                print("Making a Basic burger for customer")

class StandardBurger(Burger):
        def prepare(self):
                print("Making a Standard Burger for customer")

class PremiumBurger(Burger):
        def prepare(self):
                print("Making a Premium Burger for customer")

class BurgerFactory:
        def createburger(self,type):
                if type.lower()=="basic":
                        return BasicBurger()
                elif type.lower()=="standard":
                        return StandardBurger()
                elif type.lower()=="premium":
                        return PremiumBurger()
                else:
                        print("You have chose a wrong burger type")
                        return None


obj=BurgerFactory()
print("Burger type available\nBasic\nStandard\nPremium")
type=input("Enter a Burger type:")

burger=obj.createburger(type)
if burger:
        burger.prepare()