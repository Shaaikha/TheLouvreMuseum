#import ENUM library for listing the limited options available
from enum import Enum
from datetime import datetime
class EntryAge(Enum):
    ADULT = (63, "Age between 18 and 60")
    CHILD = (0, "Children: Free entry to the museum")
    TEACHERANDSTUDENTS = (0, "Teacher and students from an institution: Free entry to museum")
    SENIOR = (0, "Above age 60 (Senior): Free entry to museum")
    GROUP = (0.5, "Receive 50% discount on the original price of the ticket for groups")
    SPECIALEVENT = (None, "Special Event: Individual ticket price")

#import ENUM library for listing the limited options available
from enum import Enum
class TypeOfVisit(Enum):
    GROUP = "Group Visit"
    TOUR = "Tour Visit"
    INDIVIDUAL= "Individual Visit"
    EVENT= "Event visit"
    GALLERY= "Gallery Visit"
    EXHIBITION= "Exhibition Visit"
    SPECIALEVENT= "Special Event Visit"
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

