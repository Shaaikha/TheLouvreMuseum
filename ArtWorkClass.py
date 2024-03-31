from enum import Enum
class ArtLocation(Enum):
    """Enum for representing possible artwork locations within the Louvre Museum."""
    GALLERY = "Gallery"
    EXHIBITION_HALL = "Exhibition Hall"
    OUTDOOR_SPACE = "Outdoor Space"

class ArtWork:
  """Creating class for the artworks found in the Musuem"""
  #Adding class constructor to add the attributes for the artwork found in the musuem successfully
  def __init__(self, title="", artist="", dateOfCreation="",  historicalSignificance="", location= ArtLocation.GALLERY): #By adding self keyword we will initialize object of the class
   self._title= title
   self._artist= artist
   self._dateOfCreation= dateOfCreation
   self._historicalSignificance= historicalSignificance
   self._location= location

    # Getters
  def getTitle(self):
  #getter for title attribute
        return self._title

  def getArtist(self):
  #getter for artist attribute
        return self._artist

  def getDateOfCreation(self):
  #getter for dateOfCreation attribute
        return self._dateOfCreation

  def getHistoricalSignificance(self):
  #getter for historicalSignificance attribute
        return self._historicalSignificance

  def getLocation(self):
  #getter for location attribute
        return self._location

    # Setters
  def setTitle(self, title=""):
    #setter for title
        self._title = title

  def setArtist(self, artist=""):
    #setter for artist
        self._artist = artist

  def setDateOfCreation(self, dateOfCreation=""):
    #setter for dateOfCreation
        self._dateOfCreation = dateOfCreation

  def setHistoricalSignificance(self, historicalSignificance=""):
    #setter for historicalSignificance
        self._historicalSignificance = historicalSignificance

  def setLocation(self, location=ArtLocation.GALLERY):
    #setter for location
        self._location = location


  def displayData(self):
 # Creating a function the will define the details of the artworks presented at the louvre
   print(f"Title of Art Piece: {self._title} Artist: {self._artist}, Creation Date of Artwork:{self._dateOfCreation} , Historical Significance: {self._historicalSignificance}, Location: {self._location})")

 #For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
  def __str__(self):
   return f"ArtWork(Title of Art Piece: {self._title} Artist: {self._artist}, Creation Date of Artwork:{self._dateOfCreation} , Historical Significance: {self._historicalSignificance}, Location: {self._location.value})"
