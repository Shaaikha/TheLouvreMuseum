# Adding datetime library for better date specifying operations at the louvre
from datetime import datetime
# import ENUM library for listing the limited options available for Louvre Location including Paris and Abu Dhabi
from enum import Enum


class LouvreLocation(Enum):
    PARIS = "Paris, France"
    ABU_DHABI = "Abu Dhabi, UAE"


# Creating a class for the Louvre museum
class LouvreMuseum:
    """Creating class for the louvre musuem operations internal and external"""

    # Adding class constructor to add the attributes for the musuem successfully with protected attributes
    def __init__(self, museumFullName="", louvreLocation=LouvreLocation.ABU_DHABI, openingHours="",
                 openingDays=""):  # By adding self keyword we will initialize object of the class
        self._artwork = []  # A list that Illustrates the composition link between artwork and the louvre musuem
        self._employees = []  # A list that Illustrates the composition link between employees and the louvre musuem
        self._securitySystem = []  # A list that Illustrates the composition link between securitySystem and the louvre musuem
        self._facilities = []  # A list that Illustrates the composition link between facilities and the louvre musuem
        self._exhibition = []  # A list that Illustrates the composition link between exhibition and the louvre musuem
        self._tour = []  # A list that Illustrates the composition link between tour and the louvre musuem
        self._specialEvent = []  # A list that Illustrates the composition link between special event and the louvre musuem
        self._gallery = []  # A list that Illustrates the composition link between gallery and the louvre musuem
        self._visitors = []  # A list to store instances of Visitor and show aggreation relationship between lovure museum and visitor class
        self._museumFullName = museumFullName
        self._louvreLocation = louvreLocation
        self._openingHours = openingHours
        self._openingDays = openingDays

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
            print("Employee is not Valid")

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

    def setLouvreLocation(self, louvreLocation=LouvreLocation.ABU_DHABI):
        # setter for louvreLocation
        self._louvreLocation = louvreLocation

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


# Creating Enumrator for ArtLocation options
from enum import Enum


class ArtLocation(Enum):
    # Enum for representing possible artwork locations within the Louvre Museum
    GALLERY = "Gallery"
    EXHIBITION_HALL = "Exhibition Hall"
    OUTDOOR_SPACE = "Outdoor Space"


class ArtWork:
    """Creating class for the artworks found in the Musuem"""

    # Adding class constructor to add the attributes for the artwork found in the musuem successfully with protected attributes
    def __init__(self, title="", artist="", dateOfCreation="", historicalSignificance="",
                 location=ArtLocation.GALLERY):  # By adding self keyword we will initialize object of the class
        self._title = title
        self._artist = artist
        self._dateOfCreation = dateOfCreation
        self._historicalSignificance = historicalSignificance
        self._location = location

        # Getters

    def getTitle(self):
        # getter for title attribute
        return self._title

    def getArtist(self):
        # getter for artist attribute
        return self._artist

    def getDateOfCreation(self):
        # getter for dateOfCreation attribute
        return self._dateOfCreation

    def getHistoricalSignificance(self):
        # getter for historicalSignificance attribute
        return self._historicalSignificance

    def getLocation(self):
        # getter for location attribute
        return self._location

    # Setters
    def setTitle(self, title=""):
        # setter for title
        self._title = title

    def setArtist(self, artist=""):
        # setter for artist
        self._artist = artist

    def setDateOfCreation(self, dateOfCreation=""):
        # setter for dateOfCreation
        self._dateOfCreation = dateOfCreation

    def setHistoricalSignificance(self, historicalSignificance=""):
        # setter for historicalSignificance
        self._historicalSignificance = historicalSignificance

    def setLocation(self, location=ArtLocation.GALLERY):
        # setter for location
        self._location = location

    def displayData(self):
        # Creating a function the will define the details of the artworks presented at the louvre
        print(
            f"Title of Art Piece: {self._title} Artist: {self._artist}, Creation Date of Artwork:{self._dateOfCreation} , Historical Significance: {self._historicalSignificance}, Location: {self._location})")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"ArtWork(Title of Art Piece: {self._title} Artist: {self._artist}, Creation Date of Artwork:{self._dateOfCreation} , Historical Significance: {self._historicalSignificance}, Location: {self._location.value})"


class Artifacts(ArtWork):
    """Creating class for the artworks found in the Musuem"""

    # Adding class constructor to add the attributes for the artwork found in the musuem successfully for private data
    def __init__(self, title="", artist="", dateOfCreation="", historicalSignificance="", location=ArtLocation.GALLERY,
                 yearFound="", description=""):  # By adding self keyword we will initialize object of the class
        super().__init__(title, artist, dateOfCreation, historicalSignificance,
                         location)  # By using the super() function it will pass the attributes of the parent class of Artworks
        self.__yearFound = yearFound
        self.__description = description

        # Getters

    def getYearFound(self):
        return self.__yearFound

    def getDescription(self):
        return self.__description

    # Setters
    def setYearFound(self, yearFound=""):
        self.__yearFound = yearFound

    def setDescription(self, description=""):
        self.__description = description

    # Creating a function the will show the caring method of the artworks presented at the louvre
    def caringMethod(self, newMethod):
        self._caringMethod = newMethod  # Change the caring method
        print(f"New Caring method for '{self._title}': {self._caringMethod}")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return super().__str__() + f"Artifacts(Artifact Year Found: {self.__yearFound} Description of Artifact: {self.__description})"


class Employee:
    """Creating class for the louvre musuem employees"""

    # Adding class constructor to add the attributes for the musuem successfully for protected data
    def __init__(self, employeeID="", workingHours="", firstName="", lastName="",
                 nationality=""):  # By adding self keyword we will initialize object of the class
        self._employeeID = employeeID
        self._workingHours = workingHours
        self._firstName = firstName
        self._lastName = lastName
        self._nationality = nationality

        # Getter for employeeID

    def getEmployeeID(self):
        # getter for employeeID
        return self._employeeID

    # Setter for employeeID
    def setEmployeeID(self, employeeID=""):
        # setter for employeeID
        self._employeeID = employeeID

    # Getter for workingHours
    def getWorkingHours(self):
        # getter for workingHours
        return self._workingHours

    # Setter for workingHours
    def setWorkingHours(self, workingHours=""):
        # setter for workingHours
        self._workingHours = workingHours

    # Getter for firstName
    def getFirstName(self):
        # getter for firstName
        return self._firstName

    # Setter for firstName
    def setFirstName(self, firstName=""):
        # setter for firstName
        self._firstName = firstName

    # Getter for lastName
    def getLastName(self):
        # getter for lastName
        return self._lastName

    # Setter for lastName
    def setLastName(self, lastName=""):
        # setter for lastName
        self._lastName = lastName

    # Getter for nationality
    def getNationality(self):
        # getter for nationality
        return self._nationality

    # Setter for nationality
    def setNationality(self, nationality=""):
        # setter for nationality
        self._nationality = nationality

    def calculateSalary(self, hourWage):
        # Creating a function the will calculate employee salary using exception handling try and except
        try:
            salary = int(self._workingHours) * hourWage
            print(f"Total Salary for {self._firstName} {self._lastName}: {salary}")
        except ValueError:
            print("Your input for working hours is invalid")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"Employee(ID: {self._employeeID} Working Hours: {self._workingHours}, Name:{self._firstName} {self._lastName}, Employee Nationality: {self._nationality})"


# Class for enumrating the departements the managers work for
class ManagerDep(Enum):
    IT = "IT Departement"
    MARKETING = "Marketing Departement"
    FINANCE = "Finanace Departement"


class Manager(Employee):
    """Creating class for the managers found in the Musuem"""

    # Adding class constructor to add the attributes for the managers working in the musuem successfully for private data
    def __init__(self, employeeID="", workingHours="", firstName="", lastName="", nationality="",
                 departement=ManagerDep.IT,
                 yearsOfWorking=0):  # By adding self keyword we will initialize object of the class
        super().__init__(employeeID="", workingHours="", firstName="", lastName="",
                         nationality="")  # By using the super() function it will pass the attributes of the parent class of Artworks
        self.__departement = departement
        self.__yearsOfWorking = yearsOfWorking

        # Getters

    def getDepartment(self):
        # getter for department
        return self.__department

    def getYearsOfWorking(self):
        # getter for yearsOfWorking
        return self.__yearsOfWorking

    # Setters
    def setDepartment(self, department=ManagerDep.IT):
        # setter for department
        self.__department = department

    def setYearsOfWorking(self, yearsOfWorking=''):
        # setter for yearsOfWorking
        self.__yearsOfWorking = yearsOfWorking

    def fireManager(self, fireManager):
        # Creating a function to fire a manager at the louvre
        self.__isActive = False
        print(f"Manager {self._firstName} {self._lastName} has been fired.")


    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return super().__str__() + f"Manager(Manager Departement: {self.__departement.value} ,Years Of Working {self.__yearsOfWorking})"


from enum import Enum


# Enumrating the artkeeper expertise
class ExpertIn(Enum):
    WOOD = "Expert in wood Material"
    STEEL = "Expert in steel Material"
    PAPER = "Expert in paper Material"


class ArtKeeper(Employee):
    """Creating class for the Art Keepers found in the Musuem"""

    # Adding class constructor to add the attributes for the managers working in the musuem successfully
    def __init__(self, employeeID="", workingHours="", firstName="", lastName="", nationality="",
                 expertise=ExpertIn.WOOD,
                 benefits=""):  # By adding self keyword we will initialize object of the class for private data
        super().__init__(employeeID="", workingHours="", firstName="", lastName="",
                         nationality="")  # By using the super() function it will pass the attributes of the parent class of Artworks
        self.__expertise = expertise
        self.__benefits = benefits
        self.__artKeepers = []

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
        # Creating a function to add artkeepers at the louvre
        if isinstance(artKeeper, ArtKeeper):
            self.__artKeepers.append(artKeeper)
            print(f"Added Art Keeper {artKeeper._firstName} {artKeeper._lastName} to the department")
        else:
            print("No art keeper is added")

    def isArtSafe(self, materialCondition, ExpertIn):
        # Creating a function to ensure safety of artwork by art keepers
        if self.__expertise == ExpertIn.WOOD and materialCondition == "not wet":
            print(f"Art work is not safe with {self.__expertise.value}")
        else:
            print(f"Art work is safe under {self.__expertise.value}")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return super().__str__() + f"ArtKeeper(Expertise: {self.__expertise.value} ,Benefits of Art Keepers {self.__benefits})"


class TourGuide(Employee):
    """Creating class for the Tour Guide working in the Musuem"""

    # Adding class constructor to add the attributes for the managers working in the musuem successfully for private data
    def __init__(self, employeeID="", workingHours="", firstName="", lastName="", nationality="", numOfPeople=0,
                 groupID="", dateOfTour=""):  # By adding self keyword we will initialize object of the class
        super().__init__(employeeID="", workingHours="", firstName="", lastName="",
                         nationality="")  # By using the super() function it will pass the attributes of the parent class of Artworks
        self.__numOfPeople = numOfPeople
        self.__groupID = groupID
        self.__dateOfTour = dateOfTour

    # Getters
    def getNumOfPeople(self):
        # Getter for numOfPeople
        return self._numOfPeople

    def getGroupID(self):
        # Getter for groupID
        return self._groupID

    def getDateOfTour(self):
        # Getter for dateOfTour
        return self._dateOfTour

    # Setters
    def setNumOfPeople(self, numOfPeople=0):
        # Setter for numOfPeople
        self._numOfPeople = numOfPeople

    def setGroupID(self, groupID=""):
        # Setter for groupID
        self._groupID = groupID

    def setDateOfTour(self, dateOfTour=""):
        # Setter for dateOfTour
        self._dateOfTour = dateOfTour

    def addBackup(self, backupGuide):
        # Creating a function to add Back up tourist guide at the louvre
        print(
            f"Backup guide will take place of the main tour guide {backupGuide.firstName} {backupGuide.lastName} for date {self.__dateOfTour}.")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return super().__str__() + f"TourGuide(People need Guidance: {self.__numOfPeople} , Group ID {self.__groupID}, Date of the Tour{self.__dateOfTour})"


# Creating class to enumrate the options for facility
from enum import Enum


class TypeOfFacility(Enum):
    RETAIL = "Retail facility"
    DINING = "Dining facility"
    ADMINSTRATION = "Adminstration facility"
    VISITORSERVICES = "Visitor services facility"


# Creating class to enumrate the options for facility ratings
class FacilityRating(Enum):
    GOOD = "Good facility rating"
    BAD = "Bad facility rating"
    AMAZING = "Amazing facility rating"


class Facilities:
    """Creating class for the facilities found in the Musuem"""

    # Adding class constructor to add the attributes for the artwork found in the musuem successfully for protected data
    def __init__(self, facilityNumber=0, typeOfFacility=TypeOfFacility.DINING, facilityLocation="", capacity="",
                 rating=FacilityRating.GOOD):  # By adding self keyword we will initialize object of the class
        self._facilityNumber = facilityNumber
        self._typeOfFacility = typeOfFacility
        self._facilityLocation = facilityLocation
        self._capacity = capacity
        self._rating = rating

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

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"Facilities(Facilities Total Number: {self._facilityNumber}, Type Of Facility: {self._typeOfFacility}, Capacity of Facility:{self._capacity} , Rating of Facility: {self._rating})"


class SecuritySystem:
    """Creating class for the security system found in the Musuem"""

    # Adding class constructor to add the attributes for the security found in the musuem successfully for private data
    def __init__(self, securityID="", numOfCameras=0, alarms=0, viwInDark="",
                 securityCode=""):  # By adding self keyword we will initialize object of the class
        self.__securityID = securityID
        self.__numOfCameras = numOfCameras
        self.__alarms = alarms
        self.__viewInDark = viwInDark
        self.__securityCode = securityCode

        # Getters

    def getSecurityID(self):
        # Getter for securityID
        return self._securityID

    def getNumOfCameras(self):
        # Getter for numOfCameras
        return self._numOfCameras

    def getAlarms(self):
        # Getter for alarms
        return self._alarms

    def getViewInDark(self):
        # Getter for viewInDark
        return self._viewInDark

    def getSecurityCode(self):
        # Getter for securityCode
        return self._securityCode

    # Setters
    def setSecurityID(self, securityID=""):
        # Setter for securityID
        self._securityID = securityID

    def setNumOfCameras(self, numOfCameras=0):
        # Setter for numOfCameras
        self._numOfCameras = numOfCameras

    def setAlarms(self, alarms=0):
        # Setter for alarms
        self._alarms = alarms

    def setViewInDark(self, viewInDark=""):
        # Setter for viewInDark
        self._viewInDark = viewInDark

    def setSecurityCode(self, securityCode=""):
        # Setter for securityCode
        self._securityCode = securityCode

    def detectStealing(self, detectStealing):
        # Creating a function the will detect stealing at the louvre
        print("Detecting stealing sensor is activated")

    def countVisitors(self, countVisitors):
        # Creating a function the will count the total visitors at the louvre
        print("Detecting the count of visitors is activated")

    def storeVisitorData(self, storeVisitorData):
        # Creating a function the will store data of the visitors at the louvre
        print("Storage of visitor data system is applied")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"SecuritySystem(Security ID: {self.__securityID}, Number of Camera: {self.__numOfCameras}, Alarms:{self.__alarms} , Camera View in the Dark: {self.__viewInDark}, Security Passcode: {self.__securityCode})"


class Visitor:
    """Creating class for the visitors coming to the Musuem"""

    # Adding class constructor to add the attributes for the visitors found in the musuem successfully for protected data
    def __init__(self, visitorID="", firstName="", lastName="", age=0, maritalStatus="",
                 nationalIDNumber=""):  # By adding self keyword we will initialize object of the class
        self._visitorID = visitorID
        self._firstName = firstName
        self._lastName = lastName
        self._age = age
        self._maritalStatus = maritalStatus
        self._nationalIDNumber = nationalIDNumber
        self._ticket = []  # A list to illustrate the aggregation relationship between visitor class and ticket class

        # Getters

    def getVisitorID(self):
        # Getter for visitorID
        return self._visitorID

    def getFirstName(self):
        # Getter for firstName
     return self._firstName

    def getLastName(self):
        # Getter for lastName
     return self._lastName

    def getAge(self):
        # Getter for age
      return self._age

    def getMaritalStatus(self):
        # Getter for maritalStatus
        return self._maritalStatus

    def getNationalIDNumber(self):
        # Getter for nationalIDNumber
        return self._nationalIDNumber

    def getTickets(self):
        # Getter for tickets
        return self._ticket

    # Setters
    def setVisitorID(self, visitorID=""):
        # Setter for visitorID
        self._visitorID = visitorID

    def setFirstName(self, firstName=""):
        # Setter for firstName
        self._firstName = firstName

    def setLastName(self, lastName=""):
        # Setter for lastName
        self._lastName = lastName

    def setAge(self, age=0):
        # Setter for age
        self._age = age

    def setMaritalStatus(self, maritalStatus=""):
        # Setter for maritalStatus
        self._maritalStatus = maritalStatus

    def setNationalIDNumber(self, nationalIDNumber=""):
        # Setter for nationalIDNumber
        self._nationalIDNumber = nationalIDNumber

    # Creating a function to add tickets for visitors
    def has_ticket(self, ticket):
        return ticket in self._ticket

    # Creating a function to show purchase tickets for visitors
    def purchase_ticket(self, ticket):
        try:
            if not self.has_ticket(ticket):
                final_price = ticket.calculatePriceForOne()
                self._ticket.append(ticket)
                print(
                    f"{self._firstName} {self._lastName} purchased a ticket for {ticket._typeOfVisit.value} at AED{final_price}.")
            else:
                print("This visitor already has this ticket.")
        except Exception as e:  # Catch a general exception
            print(f"An error occurred while purchasing the ticket: {e}")

    # Creating a function to show receipt tickets for visitors
    def display_receipt(self):
        total = sum(ticket.calculatePriceForOne() for ticket in self._ticket)
        print(f"Receipt for {self._firstName} {self._lastName}:")
        for ticket in self._ticket:
            print(f"- Ticket for {ticket._typeOfVisit.value}, AED{ticket.calculatePriceForOne()}")
        print(f"Total: AED{total}")


    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"Visitor(Visitor ID: {self._visitorID}, Name of Visitor: {self._firstName}  {self._lastName} , age: {self._age}, Marital Status: {self._maritalStatus}, National ID Number: {self._nationalIDNumber})"


# import ENUM library for listing the limited options available
from enum import Enum
class EntryAge(Enum):
    ADULT = (63, "AdultsAbove the age of 18")
    CHILD = (0, "Children: Free entry to the museum")
    TEACHERANDSTUDENTS = (0, "Teacher and students from an institution: Free entry to museum")
    SENIOR = (0, "Above age 60 (Senior): Free entry to museum")
    GROUP = (0.5, "Receive 50% discount on the original price of the ticket for groups")
    SPECIALEVENT = (None, "Special Event: Individual ticket price")


# import ENUM library for listing the limited options available
from enum import Enum


class TypeOfVisit(Enum):
    GROUP = "Group Visit"
    TOUR = "Tour Visit"
    INDIVIDUAL = "Individual Visit"
    EVENT = "Event visit"
    GALLERY = "Gallery Visit"
    EXHIBITION = "Exhibition Visit"
    SPECIALEVENT = "Special Event Visit"


class Ticket:
    """Creating class for the tickets needed for the Musuem entery"""

    # Adding class constructor to add the attributes for the tickets required by visitors to enter the musuem successfully for protected data
    def __init__(self, visitor=None, typeOfVisit=TypeOfVisit.EXHIBITION, priceRange=EntryAge.ADULT, duration="",
                 ticketID="", expirationDate=datetime, purchasingMethod="", ticketValidityDate=datetime, location="",
                 originalPrice=63.0,
                 specialEventPrice=None):  # By adding self keyword we will initialize object of the class
        self._visitor = visitor  # passing the attributes for the visitor
        self._typeOfVisit = typeOfVisit
        self._duration = duration
        self._ticketID = ticketID
        self._expirationDate = expirationDate
        self._purchasingMethod = purchasingMethod
        self._ticketValidityDate = ticketValidityDate
        self._location = location
        self._priceRange = priceRange
        self._originalPrice = originalPrice
        self._specialEventPrice = specialEventPrice

        # Getters
        # Getter for visitor attribute

    def getVisitor(self):
        return self._visitor

    # Getter for type of visit attribute
    def getTypeOfVisit(self):
        return self._typeOfVisit

    # Getter for duration attribute
    def getDuration(self):
        return self._duration

    # Getter for ticketID attribute
    def getTicketID(self):
        return self._ticketID

    # Getter for expiration Date attribute
    def getExpirationDate(self):
        return self._expirationDate

    # Getter for purchase method attribute
    def getPurchasingMethod(self):
        return self._purchasingMethod

    # Getter for ticket validity date attribute
    def getTicketValidityDate(self):
        return self._ticketValidityDate

    # Getter for location attribute
    def getLocation(self):
        return self._location

    # Getter for price range based on entry age attribute
    def getPriceRange(self):
        return self._priceRange

    # Getter for original priceattribute
    def getOriginalPrice(self):
        return self._originalPrice

    # Getter for special event attribute
    def getSpecialEventPrice(self):
        return self._specialEventPrice

    # Setters
    # Setter for visitor attribute
    def setVisitor(self, visitor=""):
        self._visitor = visitor

    # Setter for type of visit attribute
    def setTypeOfVisit(self, typeOfVisit=TypeOfVisit.EXHIBITION):
        self._typeOfVisit = typeOfVisit

    # Setter for duration attribute
    def setDuration(self, duration=""):
        self._duration = duration

    # Setter for ticket id attribute
    def setTicketID(self, ticketID=""):
        self._ticketID = ticketID

    # Setter for expiration date attribute
    def setExpirationDate(self, expirationDate=""):
        self._expirationDate = expirationDate

    # Setter for purchasing method attribute
    def setPurchasingMethod(self, purchasingMethod=""):
        self._purchasingMethod = purchasingMethod

    # Setter for ticket validity attribute
    def setTicketValidityDate(self, ticketValidityDate=""):
        self._ticketValidityDate = ticketValidityDate

    # Setter for location attribute
    def setLocation(self, location=""):
        self._location = location

    # Setter for price range attribute
    def setPriceRange(self, priceRange=EntryAge.ADULT):
        self._priceRange = priceRange

    # Setter for original price attribute
    def setOriginalPrice(self, originalPrice=63):
        self._originalPrice = originalPrice

    # Setter for special event attribute
    def setSpecialEventPrice(self, specialEventPrice=None):
        self._specialEventPrice = specialEventPrice

    VAT = 0.05  # Including the vat rate in the UAE which is 5%, therefore, making the rate 0.05 as decimals

    def isPurchasedOnline(self):
        # This function will check is the ticket was purchased online or in Person
        return "Online" if self._purchasingMethod.lower() == "online purchase method" else "In person purchase method"


    def calculatePriceForOne(self):
        # Creating the original price for adults
        ticketprice = self._originalPrice

        # Checking for special event pricing first
        if self._typeOfVisit == TypeOfVisit.SPECIALEVENT and self._specialEventPrice is not None:
            ticketprice = self._specialEventPrice
        # Free tickets for children, teachers, students, and seniors
        elif self._visitor.getAge() < 18 or self._visitor.getAge() > 60 or \
                'teacher' in self._visitor.getMaritalStatus().lower() or \
                'student' in self._visitor.getMaritalStatus().lower():
            ticketprice = 0
        # Adding the 50% discount for group visits
        elif self._typeOfVisit == TypeOfVisit.GROUP:
            ticketprice *= 0.5
        # Applying the VAT rate to the original price
        finalPrice = ticketprice * (1 + Ticket.VAT)
        return finalPrice

    def total_price(self, num_tickets):
        # Calculates the total price for multiple tickets
        return self.calculatePriceForOne() * num_tickets

    def isNationalIDValid(self):
        # This will ensure that the visitor has a valid national ID
        return len(self._visitor.nationalIDNumber) > 0

    def isTour(self):
        # This function will specify if the ticket is for a tour or not
        return self._typeOfVisit == TypeOfVisit.TOUR


    def calculatePriceFor1(self):
        # New implementation
        ticketprice = self._originalPrice

        if self._typeOfVisit == TypeOfVisit.SPECIALEVENT and self._specialEventPrice is not None:
            ticketprice = self._specialEventPrice
        elif EntryAge[self._priceRange.name].value[1] == 'Age between 18 and 60':
            ticketprice = 0
        elif self._typeOfVisit == TypeOfVisit.GROUP:
            ticketprice *= 0.5

        finalPrice = ticketprice * (1 + Ticket.VAT)
        return finalPrice


    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"Ticket(Type Of Visit: {self._typeOfVisit.value}, Price for type of Visitor Based on Age/type of Visit: {self._priceRange.value} Duration: {self._duration},TicketID  {self._ticketID} ,Expiration Date: {self._expirationDate},Purchasing Method: {self._purchasingMethod}, Ticket Validity Date: {self._ticketValidityDate}, Location{self._location}, originalPrice: {self._originalPrice}, Special Event Price: {self._specialEventPrice})"


# import ENUM library for listing the limited options available
class ExhibitionLocation(Enum):
    PERMANENT = "permanent galleries"
    HALLS = "Exhibition halls"
    OUTDOOR = "Outdoor spaces"


class Exhibition:
    """Creating class for the exhibitions in the Musuem """

    # Adding class constructor to add the attributes for the exhibitions vistied by visitors to enter the musuem successfully with protected data
    def __init__(self, exhibitionID="", exhibitionTitle="", exhibitionTheme="", masterpieces=0,
                 exhibitionLocation=ExhibitionLocation.HALLS):  # By adding self keyword we will initialize object of the class
        self._exhibitionID = exhibitionID
        self._exhibitionTitle = exhibitionTitle
        self._exhibitionTheme = exhibitionTheme
        self._masterpieces = masterpieces
        self._exhibitionLocation = exhibitionLocation

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

    def displayExhibitionDetails(self, displayExhibitionDetails):
        # Creating a function the will allow the displaying of the exhibition details
        detailsEx = (
            f"Exhibition ID: {self._exhibitionID}, "
            f"Title: {self._exhibitionTitle}, "
            f"Theme: {self._exhibitionTheme}, "
            f"Masterpieces: {self._masterpieces}, "
            f"Location: {self._exhibitionLocation.value}"
        )
        print(detailsEx)

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"Exhibition(Exhibition ID: {self._exhibitionID},Exhibition Title: {self._exhibitionTitle}, Exhibition Theme: {self._exhibitionTheme} ,Masterpieces: {self._masterpieces}, Exhibition Location:  {self._exhibitionLocation.value})"


# import ENUM library for listing the limited options available
from enum import Enum


class GalleryLocation(Enum):
    PERMANENT = "permanent galleries"
    HALLS = "Exhibition halls"
    OUTDOOR = "Outdoor spaces"


class Gallery:
    """Creating class for the galleries in the Musuem """

    # Adding class constructor to add the attributes for the exhibitions vistied by visitors to enter the musuem successfully for protected data
    def __init__(self, galleryID="", galleryTitle="", featuredWork="", galleryTheme="", galleryDressCode="",
                 galleryLocation=GalleryLocation.PERMANENT):  # By adding self keyword we will initialize object of the class
        self._galleryID = galleryID
        self._galleryTitle = galleryTitle
        self._featuredWork = featuredWork
        self._galleryTheme = galleryTheme
        self._galleryDressCode = galleryDressCode
        self._galleryLocation = galleryLocation

        # Getters

    def getGalleryID(self):
        # Getter for galleryID
        return self._galleryID

    def getGalleryTitle(self):
        # Getter for galleryTitle
        return self._galleryTitle

    def getFeaturedWork(self):
        # Getter for featuredWork
        return self._featuredWork

    def getGalleryTheme(self):
        # Getter for galleryTheme
        return self._galleryTheme

    def getGalleryDressCode(self):
        # Getter for galleryDressCode
        return self._galleryDressCode

    def getGalleryLocation(self):
        # Getter for galleryLocation
        return self._galleryLocation

    # Setters
    def setGalleryID(self, galleryID=""):
        # Setter for galleryID
        self._galleryID = galleryID

    def setGalleryTitle(self, galleryTitle=""):
        # Setter for galleryTitle
        self._galleryTitle = galleryTitle

    def setFeaturedWork(self, featuredWork=""):
        # Setter for featuredWork
        self._featuredWork = featuredWork

    def setGalleryTheme(self, galleryTheme=""):
        # Setter for galleryTheme
        self._galleryTheme = galleryTheme

    def setGalleryDressCode(self, galleryDressCode=""):
        # Setter for galleryDressCode
        self._galleryDressCode = galleryDressCode

    def setGalleryLocation(self, galleryLocation=GalleryLocation.PERMANENT):
        # Setter for galleryLocation
        self._galleryLocation = galleryLocation

    def displayGalleryInfo(self, displayGalleryInfo):
        # Creating a function the will allow the displaying of the gellery details
        info = (
            f"Gallery ID: {self._galleryID}, "
            f"Title: {self._galleryTitle}, "
            f"Featured Work: {self._featuredWork}, "
            f"Theme: {self._galleryTheme}, "
            f"Dress Code: {self._galleryDressCode}, "
            f"Location: {self._galleryLocation.value}"
        )
        print(info)

    def updateTheme(self, updateTheme, newTheme):
        # This function is used to update the theme of the gallery
        self._galleryTheme = newTheme
        print(f"Updated Gallery Theme: {newTheme}")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"Gallery(Gallery ID: {self._galleryID},Gallery Title: {self._galleryTitle}, Featured Work: {self._featuredWork} ,Gallery Theme: {self._galleryTheme}, Gallery Dress code: {self._galleryDressCode}, Gallery Location: {self._galleryLocation.value})"


# import ENUM library for listing the limited options available
from enum import Enum


class EventLocation(Enum):
    PERMANENT = "permanent galleries"
    HALLS = "Exhibition halls"
    OUTDOOR = "Outdoor spaces"


# import ENUM library for listing the limited options available
from enum import Enum


class EventReason(Enum):
    FUND = "Fundraising"
    MUSICAL = "Musical concert"
    LIGHTSHOW = "light shows"


class SpecialEvent:
    """Creating class for the special events in the Musuem """

    # Adding class constructor to add the attributes for the events vistied by visitors to enter the musuem successfully for protected attributes
    def __init__(self, eventReason=EventReason.FUND, eventID="", nameOfEvent="", eventDescription="",
                 eventLocation=EventLocation.OUTDOOR):  # By adding self keyword we will initialize object of the class
        self._eventReason = eventReason
        self._eventID = eventID
        self._nameOfEvent = nameOfEvent
        self._eventDescription = eventDescription
        self._eventLocation = eventLocation

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

    def displayEventDetails(self, displayEventDetails):
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
        # This function will update the description of of the special events
        self._eventDescription = newDescription
        print(f"Updated Event Description: {newDescription}")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"SpecialEvent(EventReason: {self._eventReason.value},Event ID: {self._eventID}, Name Of Event: {self._nameOfEvent} ,Event Description: {self._eventDescription}, Event Location: {self._eventLocation.value})"


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

