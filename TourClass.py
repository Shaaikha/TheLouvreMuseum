#import ENUM library for listing the limited options available
from enum import Enum
class TourLocation(Enum):
  PERMANENT= "permanent galleries"
  HALLS= "Exhibition halls"
  OUTDOOR= "Outdoor spaces"

class Tour:
  """Creating class for the special events in the Musuem """
  #Adding class constructor to add the attributes for the tours vistied by visitors to enter the musuem successfully
  def __init__(self, tourID= "", guideName="", nameOfEvent="", numOfVisitors="", tourLocation= TourLocation.OUTDOOR): #By adding self keyword we will initialize object of the class
   self._tourID=tourID
   self._guideName= guideName
   self._numOfVisitors= numOfVisitors
   self._tourLocation= tourLocation


   # Getters
  def getTourID(self):
        return self._tourID

  def getGuideName(self):
        return self._guideName

  def getNameOfEvent(self):
        return self._nameOfEvent

  def getNumOfVisitors(self):
        return self._numOfVisitors

  def getTourLocation(self):
        return self._tourLocation

  def getEventDescription(self):
        return self._eventDescription

    # Setters
  def setTourID(self, tourID):
        self._tourID = tourID

  def setGuideName(self, guideName):
        self._guideName = guideName

  def setNameOfEvent(self, nameOfEvent):
        self._nameOfEvent = nameOfEvent

  def setNumOfVisitors(self, numOfVisitors):
        self._numOfVisitors = numOfVisitors

  def setTourLocation(self, tourLocation):
        self._tourLocation = tourLocation

  def setEventDescription(self, eventDescription):
        self._eventDescription = eventDescription



  def updateTourDescription(self, newDescription):
  #This function will update the description of of the tours
        self._eventDescription = newDescription
        print(f"Updated Tour Description: {newDescription}")

 #For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
  def __str__(self):
   return f"Tour(Tour ID: {self._tourID},Guide Name: {self._guideName}, Number Of Visitors: {self._numOfVisitors}, Tour Location:{self._tourLocation.value})"

