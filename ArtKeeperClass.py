#Enumrating the artkeeper expertise
from enum import Enum
class ExpertIn(Enum):
    WOOD = "Expert in wood Material"
    STEEL = "Expert in steel Material"
    PAPER = "Expert in paper Material"


class ArtKeeper(Employee):
  """Creating class for the Art Keepers found in the Musuem"""
  #Adding class constructor to add the attributes for the managers working in the musuem successfully
  def __init__(self, expertise= ExpertIn.WOOD, benefits=""): #By adding self keyword we will initialize object of the class
   super().__init__(employeeID="", workingHours="", firstName="", lastName="", nationality="")  #By using the super() function it will pass the attributes of the parent class of Artworks
   self.__expertise= expertise
   self.__benefits= benefits

    # Getters
  def getExpertise(self):
        # Getter for expertise
        return self._expertise

  def getBenefits(self):
        # Getter for benefits
        return self._benefits

    # Setters
  def setExpertise(self, expertise=ExpertIn.WOOD):
        # Setter for expertise
        self._expertise = expertise

  def setBenefits(self, benefits=""):
        # Setter for benefits
        self._benefits = benefits

  def addArtKeeper(self, artKeeper, ArtKeeper):
  #Creating a function to add artkeepers at the louvre
        if isinstance(artKeeper, ArtKeeper):
            self.__artKeepers.append(artKeeper)
            print(f"Added Art Keeper {artKeeper.firstName} {artKeeper.lastName} to the department")
        else:
            print("No art keeper is added")

  def isArtSafe(self, materialCondition, ExpertIn):
    #Creating a function to ensure safety of artwork by art keepers
   if self.__expertise == ExpertIn.WOOD and materialCondition == "not wet":
            print(f"Art work is not safe with {self.__expertise.value}")
   else:
            print(f"Art work is safe under {self.__expertise.value}")

 #For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
  def __str__(self):
    return super().__str__()+ f"ArtKeeper(Expertise: {self.__expertise.value} ,Benefits of Art Keepers {self.__benefits})"

