from enum import Enum
#import ENUM library for listing the limited options available
class ExhibitionLocation(Enum):
  PERMANENT= "permanent galleries"
  HALLS= "Exhibition halls"
  OUTDOOR= "Outdoor spaces"

class Exhibition:
  """Creating class for the exhibitions in the Musuem """
  #Adding class constructor to add the attributes for the exhibitions vistied by visitors to enter the musuem successfully
  def __init__(self, exhibitionID= "", exhibitionTitle="", exhibitionTheme="",  masterpieces=0, exhibitionLocation=ExhibitionLocation.HALLS): #By adding self keyword we will initialize object of the class
   self._exhibitionID=exhibitionID
   self._exhibitionTitle= exhibitionTitle
   self._exhibitionTheme=  exhibitionTheme
   self._masterpieces= masterpieces
   self._exhibitionLocation= exhibitionLocation


    # Getters
  def getExhibitionID(self):
        # Getter for exhibitionID
        return self._exhibitionID

  def getExhibitionTitle(self):
        # Getter for exhibitionTitle
        return self._exhibitionTitle

  def getExhibitionTheme(self):
        # Getter for exhibitionTheme
        return self._exhibitionTheme

  def getMasterpieces(self):
        # Getter for masterpieces
        return self._masterpieces

  def getExhibitionLocation(self):
        # Getter for exhibitionLocation
        return self._exhibitionLocation

    # Setters
  def setExhibitionID(self, exhibitionID):
        # Setter for exhibitionID
        self._exhibitionID = exhibitionID

  def setExhibitionTitle(self, exhibitionTitle):
        # Setter for exhibitionTitle
        self._exhibitionTitle = exhibitionTitle

  def setExhibitionTheme(self, exhibitionTheme):
        # Setter for exhibitionTheme
        self._exhibitionTheme = exhibitionTheme

  def setMasterpieces(self, masterpieces):
        # Setter for masterpieces
        self._masterpieces = masterpieces

  def setExhibitionLocation(self, exhibitionLocation):
        # Setter for exhibitionLocation
        self._exhibitionLocation = exhibitionLocation

  def displayExhibitionDetails(self,displayExhibitionDetails):
 # Creating a function the will allow the displaying of the exhibition details
        detailsEx = (
            f"Exhibition ID: {self._exhibitionID}, "
            f"Title: {self._exhibitionTitle}, "
            f"Theme: {self._exhibitionTheme}, "
            f"Masterpieces: {self._masterpieces}, "
            f"Location: {self._exhibitionLocation.value}"
        )
        print(detailsEx)


 #For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
  def __str__(self):
   return f"Exhibition(Exhibition ID: {self._exhibitionID},Exhibition Title: {self._exhibitionTitle}, Exhibition Theme: {self._exhibitionTheme} ,Masterpieces: {self._masterpieces}, Exhibition Location:  {self._exhibitionLocation.value})"

