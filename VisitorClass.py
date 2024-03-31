class Visitor:
    """Creating class for the visitors coming to the Musuem"""

    # Adding class constructor to add the attributes for the visitors found in the musuem successfully
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
        self._ticket.append(ticket)  # Ensure this is the correct attribute name
        final_price = ticket.calculatePriceForOne()  # Corrected method call
        print(
            f"{self._firstName} {self._lastName} purchased a ticket for {ticket._typeOfVisit.value} at AED{final_price}.")

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
