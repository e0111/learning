# this specific programme requires the use of date library 
import datetime 

class Character():
    def __init__(self, Name, DoB, intel, speed ):
        self.__CharacterName = Name #string
        self.__DateOfBirth = DoB #date
        self.__Intelligence = intel #real
        self.__Speed = speed #integer 
#underscore (__) represents privacy
    def GetName(self):
        return self.__CharacterName

    def GetIntelligence(self):
        return self.__Intelligence 

    def SetIntelligence(self, value):
        self.__Intelligence = value 

    def Learn(self):
        self.__Intelligence = self.__Intelligence*1.1
      # self.SetIntelligence(self.GetIntelligence()*1.1)

    def ReturnAge(self):
        return 2026 - self.__DateOfBirth.year

FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)
FirstCharacter.Learn()
print(FirstCharacter.ReturnAge(),"years old and their intelligence is", FirstCharacter.GetIntelligence())


class MagicCharacter(Character):
    def __init__(self, elem, Name, DoB, intel, speed):
        super().__init__(Name, DoB, intel, speed)
        self.__Element = elem 

    def Learn(self):
        elemnt = self.__Element 
        if elemnt == 'fire' or elemnt == 'water':
            super().SetIntelligence(super().GetIntelligence()*1.2)
        elif elemnt == 'earth':
            super().SetIntelligence(super().GetIntelligence()*1.3)
        else:
            super().SetIntelligence(super().GetIntelligence()*1.1)

FirstMagic = MagicCharacter('fire','LIGHT', datetime.date(2018, 3, 3), 75, 22)
FirstMagic.Learn()
print(FirstMagic.ReturnAge(),"years old and their intelligence is", FirstMagic.GetIntelligence())



