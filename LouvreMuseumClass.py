from EmployeeClass import Employee
#import ENUM library for listing the limited options available
from enum import Enum
class LouvreLocation(Enum):
    PARIS = "Paris, France"
    ABU_DHABI = "Abu Dhabi, UAE"

class LouvreMuseum:
  """Creating class for the louvre musuem operations internal and external"""
  #Adding class constructor to add the attributes for the musuem successfully
  def __init__(self, museumFullName="", louvreLocation= LouvreLocation.ABU_DHABI, openingHours="", openingDays=""): #By adding self keyword we will initialize object of the class
   self._artwork= [] # A list that Illustrates the composition link between artwork and the louvre musuem
   self._employees = []  # A list that Illustrates the composition link between employees and the louvre musuem
   self._securitySystem = []  # A list that Illustrates the composition link between securitySystem and the louvre musuem
   self._facilities = []  # A list that Illustrates the composition link between facilities and the louvre musuem
   self._exhibition= []  # A list that Illustrates the composition link between exhibition and the louvre musuem
   self._tour = []  # A list that Illustrates the composition link between tour and the louvre musuem
   self._specialEvent = []  # A list that Illustrates the composition link between special event and the louvre musuem
   self._gallery = []  # A list that Illustrates the composition link between gallery and the louvre musuem
   self._visitors= []# A list to store instances of Visitor and show aggreation relationship between lovure museum and visitor class
   self._museumFullName= museumFullName
   self._louvreLocation= louvreLocation
   self._openingHours= openingHours
   self._openingDays= openingDays

  # This method will be used to add more arkworks or remove artworks to the museum as it shows that the artwork belongs to the musuem due to composition
  def add_artwork(self, artwork):
      self._artwork.append(artwork)
      print(f"Artwork '{artwork._title}' by {artwork._artist} has been added to the Louvre museum, Abu Dhabi")

  def remove_artwork(self, artwork):
      try:
          self._artwork.remove(artwork)
          print(f"Artwork '{artwork._title}' by {artwork._artist} has been removed from the museum.")
      except ValueError:
          print("Artwork that needs to be removed was not found in the museum collection")

  # Method for Adding And Removing security Systems
  def addSecuritySystem(self, securitySystem):
      self._securitySystem.append(securitySystem)

  def removeSecuritySystem(self, securitySystem):
      self._securitySystem.remove(securitySystem)

      # This method will add facility or remove facility at the louvre museum

  def add_facility(self, facility):
      self._facilities.append(facility)

  def remove_facility(self, facility):
      self._facilities.remove(facility)

      # This method will add visitor or remove at the louvre museum

  def register_visitor(self, visitor):
      self._visitors.append(visitor)

  def unregister_visitor(self, visitor):
      self._visitors.remove(visitor)

      # This method will add an employee at the louvre museum

  def add_employee(self, employee):
      if isinstance(employee, Employee):
          self._employees.append(employee)
      else:
          print("The provided object is not a valid Employee instance.")

      # This method will add and remove exhibtion at the louvre museum

  def addExhibition(self, exhibition):
      self._exhibition.append(exhibition)
      print(f"There is a New Exhibition Opening: {exhibition._exhibitionTitle}")

  def removeExhibition(self, exhibition):
      self._exhibition.remove(exhibition)
      print(f"There is a New removed Exhibition: {exhibition._exhibitionTitle}")

  # This method will add and remove tour at the louvre museum
  def addTour(self, tour, Tour):
      if isinstance(tour, Tour):
          self._tour.append(tour)

  def removeTour(self, tour):
      if tour in self._tour:
          self._tour.remove(tour)

  # This method will add and remove special event at the louvre museum
  def addSpecialEvent(self, event):
      self._specialEvent.append(event)
      print(f"There is a New Special Event Opening: {event._nameOfEvent}")

  def removeSpecialEvent(self, event):
      self._specialEvent.remove(event)
      print(f"There is a New removal of Special Event Opening: {event._nameOfEvent}")

  # Getters for Louvre Musuem class for reading
  # getter for museumfull name attribute
  def getMuseumFullName(self):
      return self._museumFullName

  # getter for louvrelocation attribute
  def getLouvreLocation(self):
      return self._louvreLocation

  # getter for opening hours attribute
  def getOpeningHours(self):
      return self._openingHours

  # getter for opening days attribute
  def getOpeningDays(self):
      return self._openingDays

  # Setters for Louvre Museum for editing
  def setMuseumFullName(self, museumFullName=""):
      self._museumFullName = museumFullName

  def setLouvreLocation(self, louvreLocation =LouvreLocation.ABU_DHABI):
      # setter for louvreLocation
      self._louvreLocation= louvreLocation

  def setOpeningHours(self, openingHours=""):
      # setter for openingHours
      self._openingHours = openingHours

  def setOpeningDays(self, openingDays=""):
      # setter for openingDays
      self._openingDays = openingDays

  def displayInfo(self, musuemFullName, louvreLocation, openingHours, openingDays):
      # Creating a function the will define the details of the Louvre meseum
      print(
          f"Museum Name: {self._museumFullName} Location: {self._louvreLocation}, Opening Hours:{self._openingHours} , Opening Days: {self._openingDays})")

  # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
  def __str__(self):
      return f"LouvreMuseum(Museum Name: {self._museumFullName} Location: {self._louvreLocation.value}, Opening Hours:{self._openingHours} , Opening Days: {self._openingDays})"
