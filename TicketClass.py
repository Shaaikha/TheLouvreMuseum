# import ENUM library for listing the limited options available
from enum import Enum


class EntryAge(Enum):
    ADULT = (63, "Age between 18 and 60")
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

    # Adding class constructor to add the attributes for the tickets required by visitors to enter the musuem successfully
    def __init__(self, visitor="", typeOfVisit=TypeOfVisit.EXHIBITION, priceRange=EntryAge.ADULT, duration="",
                 ticketID="", expirationDate="", purchasingMethod="", ticketValidityDate="", location="",
                 originalPrice=63,
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

    def getVisitor(self):
        return self._visitor

    def getTypeOfVisit(self):
        return self._typeOfVisit

    def getDuration(self):
        return self._duration

    def getTicketID(self):
        return self._ticketID

    def getExpirationDate(self):
        return self._expirationDate

    def getPurchasingMethod(self):
        return self._purchasingMethod

    def getTicketValidityDate(self):
        return self._ticketValidityDate

    def getLocation(self):
        return self._location

    def getPriceRange(self):
        return self._priceRange

    def getOriginalPrice(self):
        return self._originalPrice

    def getSpecialEventPrice(self):
        return self._specialEventPrice

    # Setters
    def setVisitor(self, visitor=""):
        self._visitor = visitor

    def setTypeOfVisit(self, typeOfVisit=TypeOfVisit.EXHIBITION):
        self._typeOfVisit = typeOfVisit

    def setDuration(self, duration=""):
        self._duration = duration

    def setTicketID(self, ticketID=""):
        self._ticketID = ticketID

    def setExpirationDate(self, expirationDate=""):
        self._expirationDate = expirationDate

    def setPurchasingMethod(self, purchasingMethod=""):
        self._purchasingMethod = purchasingMethod

    def setTicketValidityDate(self, ticketValidityDate=""):
        self._ticketValidityDate = ticketValidityDate

    def setLocation(self, location=""):
        self._location = location

    def setPriceRange(self, priceRange=EntryAge.ADULT):
        self._priceRange = priceRange

    def setOriginalPrice(self, originalPrice=63):
        self._originalPrice = originalPrice

    def setSpecialEventPrice(self, specialEventPrice=None):
        self._specialEventPrice = specialEventPrice

    VAT = 0.05  # Including the vat rate in the UAE which is 5%, therefore, making the rate 0.05 as decimals

    def isPurchasedOnline(self):
        # This function will check is the ticket was purchased online or in Person
        return "Online" if self._purchasingMethod.lower() == "online purchase method" else "In person purchase method"

    def calculatePriceForOne(self):
        # Default price for adults
        ticketprice = self._originalPrice

        # Check for special event pricing first
        if self._typeOfVisit == TypeOfVisit.SPECIALEVENT and self._specialEventPrice is not None:
            ticketprice = self._specialEventPrice
        # Free tickets for children, teachers, students, and seniors
        elif self._visitor._age < 18 or self._visitor._age > 60 or self._visitor._maritalStatus.lower() in ['teacher',
                                                                                                            'student']:
            ticketprice = 0
        # 50% discount for group visits
        elif self._typeOfVisit == TypeOfVisit.GROUP:
            ticketprice *= 0.5

        # Apply VAT
        finalPrice = ticketprice * (1 + Ticket.VAT)
        return finalPrice

    def total_price(self, num_tickets):
        # Calculates the total price for multiple tickets
        return self.calculatePriceForOne() * num_tickets

    def isNationalIDValid(self):
        # This will ensure that the visitor has a valid national ID
        return len(self.visitor.nationalIDNumber) > 0

    def isTour(self):
        # This function will specify if the ticket is for a tour or not
        return self.typeOfVisit == TypeOfVisit.TOUR

    def calculatePriceFor1(self):
        if self._typeOfVisit == TypeOfVisit.SPECIALEVENT and self._specialEventPrice is not None:
            price = self._specialEventPrice
        elif self._visitor._age < 18 or self._visitor._age > 60 or 'teacher' in self._visitor._maritalStatus.lower() or 'student' in self._visitor._maritalStatus.lower():
            price = 0  # Free entry for children, seniors, teachers, and students
        elif self._typeOfVisit == TypeOfVisit.GROUP:
            price = EntryAge.ADULT.value[0] * EntryAge.GROUP.value[0]  # 50% discount for groups
        else:
            price = EntryAge.ADULT.value[0]  # Default adult price

        final_price = price * (1 + Ticket.VAT)  # Apply VAT
        return final_price

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"Ticket(Type Of Visit: {self._typeOfVisit.value}, Price for type of Visitor Based on Age/type of Visit: {self._priceRange.value} Duration: {self._duration},TicketID  {self._ticketID} ,Expiration Date: {self._expirationDate},Purchasing Method: {self._purchasingMethod}, Ticket Validity Date: {self._ticketValidityDate}, Location{self._location.value}, originalPrice: {self._orginalPrice}, Special Event Price: {self._specialEventPrice})"
