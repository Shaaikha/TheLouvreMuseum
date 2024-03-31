from enum import Enum
class TypeOfFacility(Enum):
    RETAIL = "Retail facility"
    DINING = "Dining facility"
    ADMINSTRATION= "Adminstration facility"
    VISITORSERVICES= "Visitor services facility"

class FacilityRating(Enum):
    GOOD = "Good facility rating"
    BAD = "Bad facility rating"
    AMAZING= "Amazing facility rating"


class Facilities:
  """Creating class for the facilities found in the Musuem"""
  #Adding class constructor to add the attributes for the artwork found in the musuem successfully
  def __init__(self, facilityNumber=0, typeOfFacility= TypeOfFacility.DINING, facilityLocation="",  capacity="", rating= FacilityRating.GOOD): #By adding self keyword we will initialize object of the class
   self._facilityNumber= facilityNumber
   self._typeOfFacility= typeOfFacility
   self._facilityLocation= facilityLocation
   self._capacity= capacity
   self._rating= rating

   # Getters
  def getFacilityNumber(self):
        # Getter for facilityNumber
        return self._facilityNumber

  def getTypeOfFacility(self):
        # Getter for typeOfFacility
        return self._typeOfFacility

  def getFacilityLocation(self):
        # Getter for facilityLocation
        return self._facilityLocation

  def getCapacity(self):
        # Getter for capacity
        return self._capacity

  def getRating(self):
        # Getter for rating
        return self._rating

    # Setters
  def setFacilityNumber(self, facilityNumber):
        # Setter for facilityNumber
        self._facilityNumber = facilityNumber

  def setTypeOfFacility(self, typeOfFacility):
        # Setter for typeOfFacility
        self._typeOfFacility = typeOfFacility

  def setFacilityLocation(self, facilityLocation):
        # Setter for facilityLocation
        self._facilityLocation = facilityLocation

  def setCapacity(self, capacity):
        # Setter for capacity
        self._capacity = capacity

  def setRating(self, rating):
        # Setter for rating
        self._rating = rating

 #For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
  def __str__(self):
   return f"Facilities(Facilities Total Number: {self._facilityNumber}, Type Of Facility: {self._typeOfFacility}, Capacity of Facility:{self._capacity} , Rating of Facility: {self._rating})"

