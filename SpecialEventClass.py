#import ENUM library for listing the limited options available
from enum import Enum
class EventLocation(Enum):
  PERMANENT= "permanent galleries"
  HALLS= "Exhibition halls"
  OUTDOOR= "Outdoor spaces"

#import ENUM library for listing the limited options available
from enum import Enum
class EventReason(Enum):
  FUND="Fundraising"
  MUSICAL= "Musical concert"
  LIGHTSHOW= "light shows"

class SpecialEvent:
  """Creating class for the special events in the Musuem """
  #Adding class constructor to add the attributes for the events vistied by visitors to enter the musuem successfully
  def __init__(self, eventReason= EventReason.FUND, eventID="", nameOfEvent="",  eventDescription="", eventLocation= EventLocation.OUTDOOR): #By adding self keyword we will initialize object of the class
   self._eventReason=eventReason
   self._eventID= eventID
   self._nameOfEvent= nameOfEvent
   self._eventDescription= eventDescription
   self._eventLocation= eventLocation

    # Getters
  def getEventReason(self):
        # Getter for eventReason
        return self._eventReason

  def getEventID(self):
        # Getter for eventID
        return self._eventID

  def getNameOfEvent(self):
        # Getter for nameOfEvent
        return self._nameOfEvent

  def getEventDescription(self):
        # Getter for eventDescription
        return self._eventDescription

  def getEventLocation(self):
        # Getter for eventLocation
        return self._eventLocation

    # Setters
  def setEventReason(self, eventReason=EventReason.FUND):
        # Setter for eventReason
        self._eventReason = eventReason

  def setEventID(self, eventID=""):
        # Setter for eventID
        self._eventID = eventID

  def setNameOfEvent(self, nameOfEvent=""):
        # Setter for nameOfEvent
        self._nameOfEvent = nameOfEvent

  def setEventDescription(self, eventDescription=""):
        # Setter for eventDescription
        self._eventDescription = eventDescription

  def setEventLocation(self, eventLocation=EventLocation.OUTDOOR):
        # Setter for eventLocation
        self._eventLocation = eventLocation

  def displayEventDetails(self,displayEventDetails):
 # Creating a function the will allow the displaying of the gellery details
        details = (
            f"Event ID: {self._eventID}, "
            f"Name: {self._nameOfEvent}, "
            f"Reason: {self._eventReason.value}, "
            f"Description: {self._eventDescription}, "
            f"Location: {self._eventLocation.value}"
        )
        print(details)

  def updateDescription(self, newDescription):
  #This function will update the description of of the special events
        self._eventDescription = newDescription
        print(f"Updated Event Description: {newDescription}")


 #For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
  def __str__(self):
   return f"SpecialEvent(EventReason: {self._eventReason.value},Event ID: {self._eventID}, Name Of Event: {self._nameOfEvent} ,Event Description: {self._eventDescription}, Event Location: {self._eventLocation.value})"

