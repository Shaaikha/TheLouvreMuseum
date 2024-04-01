# import ENUM library for listing the limited options available
from enum import Enum


class TourLocation(Enum):
    PERMANENT = "permanent galleries"
    HALLS = "Exhibition halls"
    OUTDOOR = "Outdoor spaces"


class Tour:
    """Creating class for the special events in the Musuem """

    # Adding class constructor to add the attributes for the tours vistied by visitors to enter the musuem successfully by protected attributes
    def __init__(self, tourID="", guideName="", nameOfEvent="", numOfVisitors="",
                 tourLocation=TourLocation.OUTDOOR):  # By adding self keyword we will initialize object of the class
        self._tourID = tourID
        self._guideName = guideName
        self._numOfVisitors = numOfVisitors
        self._tourLocation = tourLocation

        # Getters

    # Getters for tour ID attribute
    def getTourID(self):
        return self._tourID

    # Getters for guide name attribute
    def getGuideName(self):
        return self._guideName

    # Getters for name of event attribute
    def getNameOfEvent(self):
        return self._nameOfEvent

    # Getters for number of visitors attribute
    def getNumOfVisitors(self):
        return self._numOfVisitors

    # Getters for tour location attribute
    def getTourLocation(self):
        return self._tourLocation

    # Getters for event description attribute
    def getEventDescription(self):
        return self._eventDescription

    # Setters
    # Setters for tour IDattribute
    def setTourID(self, tourID):
        self._tourID = tourID

    # Setters for guide name attribute
    def setGuideName(self, guideName):
        self._guideName = guideName

    # Setters for name of event attribute
    def setNameOfEvent(self, nameOfEvent):
        self._nameOfEvent = nameOfEvent

    # Setters for number of visitors attribute
    def setNumOfVisitors(self, numOfVisitors):
        self._numOfVisitors = numOfVisitors

    # Setters for tour location attribute
    def setTourLocation(self, tourLocation):
        self._tourLocation = tourLocation

    # Setters for event description attribute
    def setEventDescription(self, eventDescription):
        self._eventDescription = eventDescription

    def updateTourDescription(self, newDescription):
        # This function will update the description of of the tours
        self._eventDescription = newDescription
        print(f"Updated Tour Description: {newDescription}")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"Tour(Tour ID: {self._tourID},Guide Name: {self._guideName}, Number Of Visitors: {self._numOfVisitors}, Tour Location:{self._tourLocation.value})"

