from abc import ABC, abstractmethod
class Character:
    @abstractmethod
    def getAbilities()->str:
        pass

class Mario(Character):
    def getAbilities(self)->str:
        return "Mario"

class CharacterDecorator(Character):
    def __init__(self, character:Character):
        self._character = character

class HeightUp(CharacterDecorator):
    def __init__(self, c: Character):
        super().__init__(c)

    def getAbilities(self) -> str:
        return self._character.getAbilities() + ", Height Up"

class GunPowerUp(CharacterDecorator):
    def __init__(self, c: Character):
        super().__init__(c)

    def getAbilities(self) -> str:
        return self._character.getAbilities() + ", Gun Power Up"
    
class StarPowerUp(CharacterDecorator):
    def __init__(self,c: Character):
        super().__init__(c)
    
    def getAbilities(self)-> str:
        return self._character.getAbilities() + ", Star Power Up"

mario=Mario()
print(f"Basic Character: {mario.getAbilities()}")
mario=HeightUp(mario)
print(f'Height Up Character: {mario.getAbilities()}')

mario=GunPowerUp(mario)
print(f'Gun Power Up Character: {mario.getAbilities()}')

mario=StarPowerUp(mario)
print(f'Star Power Up Character: {mario.getAbilities()}')
     