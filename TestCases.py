from LouvreMuseumClass import LouvreMuseum
from ArtWorkClass import ArtWork
from TicketClass import Ticket
from ArtifactClass import Artifacts
from VisitorClass import Visitor
from TourGuideClass import TourGuide
from TourClass import Tour
from ExhibitionClass import Exhibition
from SpecialEventClass import SpecialEvent
from SecuritySystemClass import SecuritySystem
from ManagerClass import Manager
from GallerClass import Gallery
from FacilityClass import Facilities
from EmployeeClass import Employee
from ArtKeeperClass import ArtKeeper
from LouvreMuseumClass import LouvreLocation
from ArtWorkClass import ArtLocation
from ManagerClass import ManagerDep
from ArtKeeperClass import ExpertIn
from FacilityClass import TypeOfFacility
from FacilityClass import FacilityRating
from TicketClass import EntryAge, TypeOfVisit
from ExhibitionClass import ExhibitionLocation
from TourClass import TourLocation
from SpecialEventClass import EventLocation
from GallerClass import GalleryLocation
from SpecialEventClass import EventReason

#Creating a test case for adding a new artwork to the louvre museum
museum = LouvreMuseum()
new_art = ArtWork("Starry Night", "Vincent van Gogh", "1889", "Post Impressionism", "Permanent Collection")
museum.add_artwork(new_art)

#Adding the museum class for refrence
louvre_museum = LouvreMuseum(museumFullName="Louvre Museum", louvreLocation=LouvreLocation.ABU_DHABI, openingHours="09:00 - 18:00", openingDays="Tuesday to Sunday")

#Adding the exhibition class for refrence
exhibition = Exhibition(exhibitionID="EXH123", exhibitionTitle="Fancy Art", exhibitionTheme="Pastel", masterpieces=200, exhibitionLocation=ExhibitionLocation.HALLS)

#Adding the exhibition class for special event
event = SpecialEvent(eventID="EVE123", nameOfEvent="NIGHTY NIGHT at the Museum", eventDescription="Night full of art and joy", eventReason=EventReason.FUND, eventLocation=EventLocation.OUTDOOR)

#Adding both exhibition and event to the museum
louvre_museum.addExhibition(exhibition)
louvre_museum.addSpecialEvent(event)


#Defining the visitor and TypeOfVisit through adding objects and attributes
adultVisitor = Visitor("123", "Hamda", "Abdulla", 20, "Single", "1234567890")
childVisitor = Visitor("234", "Marwa", "AlAli", 10, "Student", "9876543210")
groupVisitor= Visitor("456", "Group", "Visit", 40, "Married and Single Visitors", "03476467")
specialVisitor= Visitor("678", "Event", "Visit", 40, "Married and Single Visitors", "03476467")
tourVisitor= Visitor("8910", "Tour", "Visit", 40, "Married and Single Visitors", "03476467")

#Developing the tickets
adultTicket = Ticket(adultVisitor, TypeOfVisit.INDIVIDUAL)
childTicket = Ticket(childVisitor, TypeOfVisit.INDIVIDUAL)
groupTicket= Ticket(groupVisitor, TypeOfVisit.GROUP)
eventTicket= Ticket(specialVisitor, TypeOfVisit.SPECIALEVENT)
tourTicket= Ticket(tourVisitor, TypeOfVisit.SPECIALEVENT)

# Calculating ticket prices
print(f"Adult ticket price: AED{adultTicket.calculatePriceForOne()}")
print(f"Child ticket price: AED{childTicket.calculatePriceForOne()}")
print(f"Group ticket price: AED{groupTicket.calculatePriceForOne()}")
print(f"Special Event ticket price for an individual: AED{eventTicket.calculatePriceForOne()}")
print(f"Tour ticket price for an event: AED{tourTicket.calculatePriceForOne()}")


#Using Enum definitions for TypeOfVisit to find the total recipt of the tickets
visitor = Visitor("11111", "Shaikha", "Alkaabi", 19, "Single", "1372856856")
ticket1 = Ticket(visitor, TypeOfVisit.INDIVIDUAL, 63.0)
ticket2 = Ticket(visitor, TypeOfVisit.SPECIALEVENT, specialEventPrice=120)


#Priniting the total price of tickets
visitor.purchase_ticket(ticket1)
visitor.purchase_ticket(ticket2)
visitor.display_receipt()


#Creating the instances for the visitor
adult_visitor = Visitor("01222", "Mohammed", "Alzaabi", 35, "Single", "92948748969756")
senior_visitor = Visitor("0663636", "Shamma", "Aldhaheri", 65, "Single", "84748953837569")

#Creating a special event ticket for an adult
special_event_ticket = Ticket(adult_visitor, TypeOfVisit.SPECIALEVENT, specialEventPrice=120)

#Creating a group visit ticket, assuming the group is visiting a regular exhibition
group_ticket = Ticket(adult_visitor, TypeOfVisit.GROUP)

#Adding the purchase the tickets
adult_visitor.purchase_ticket(special_event_ticket)
senior_visitor.purchase_ticket(group_ticket)  # Demonstrating the group discount and age based free entry

#Displaying the receipts for visitors
adult_visitor.display_receipt()
senior_visitor.display_receipt()


# Creating a test case for adding a new artwork to the louvre museum
def test_remove():
    # Add ArtWork object
    museum = LouvreMuseum()
    new_art = ArtWork("Starry Night", "Vincent van Gogh", "1889", "Post Impressionism", "Permanent Collection")
    museum.add_artwork(new_art)
    # Remove the artwork
    museum.remove_artwork(new_art)

    # Check if the artwork was removed perfectly
    is_removed = new_art not in museum._artwork
    assert is_removed, "Artwork was not successfully removed from the museum."

    # Display the test result
    print(
        f"REMOVING ARTWORK, Test Passed: Artwork '{new_art.getTitle()}' was successfully removed from the Louvre Museum.")


# Call the test case
test_remove()


def test_ticket_data():
    # Create visitors for different categories
    adult_visitor = Visitor("123344", "Saeed", "Rashed", 21, "Single", "1234567890")
    senior_visitor = Visitor("34767856", "Mohammed Ali", "Al Hammadi", 68, "Married", "0987654321")
    group_visitor = Visitor("3839759", "Group", "Visit", 68, "Married and Single", "0987654321")

    # Create tickets for different visit types
    tour_ticket = Ticket(visitor=adult_visitor, typeOfVisit=TypeOfVisit.TOUR, priceRange=EntryAge.ADULT,
                         duration="2 hours", ticketID="T001", expirationDate="2024-05-01", purchasingMethod="Online",
                         ticketValidityDate="2024-04-20", location=TourLocation.HALLS, originalPrice=63.0)
    special_event_ticket = Ticket(visitor=senior_visitor, typeOfVisit=TypeOfVisit.SPECIALEVENT,
                                  priceRange=EntryAge.SENIOR, duration="3 hours", ticketID="E001",
                                  expirationDate="2024-12-01", purchasingMethod="In-person",
                                  ticketValidityDate="2024-11-25", location=EventLocation.OUTDOOR, originalPrice=63.0,
                                  specialEventPrice=150.0)
    group_ticket = Ticket(visitor=adult_visitor, typeOfVisit=TypeOfVisit.GROUP, priceRange=EntryAge.GROUP,
                          duration="6 hours", ticketID="T001", expirationDate="2024-05-03",
                          purchasingMethod="In-person", ticketValidityDate="2024-04-20", location=TourLocation.HALLS,
                          originalPrice=63.0)

    # Illustrate all the ticket data
    tickets = [tour_ticket, special_event_ticket, group_ticket]
    for ticket in tickets:
        print(
            f"Ticket ID: {ticket.getTicketID()}, Visitor: {ticket.getVisitor().getFirstName()} {ticket.getVisitor().getLastName()}, Type of Visit: {ticket.getTypeOfVisit().value}, Price: {ticket.calculatePriceForOne()} AED, Verifying Price: {ticket.calculatePriceFor1()} AED, Duration: {ticket.getDuration()}, Location: {ticket.getLocation().value}, Purchasing Method: {ticket.getPurchasingMethod()}, Validity Date: {ticket.getTicketValidityDate()}")

    # Checking if we can see the result sucessfully
    print("Test Passed: Ticket data displayed successfully")


# Execute the test case
test_ticket_data()

# Creating a test case to ensure the addition of a new artifact
museum = LouvreMuseum()
artifact = Artifacts("Egyptian Pyramid stone", "1400 BC", "1500 BC", "Created piece in ancient eygpt",
                     "Permanent Collection", "1920", "Created piece in ancient eygpt was found in a war")

museum.add_artwork(artifact)

# Verifying if the artifact was successfully added
assert artifact in museum._artwork, "Artifact was not added properly"

print("The Artifact was successfully addeed in the Louvre museum")

museum = LouvreMuseum()
visitor = Visitor("73468764", "Alya", "Rami", 38, "Married", "987654321")

# First we will show the registered visitor
museum.register_visitor(visitor)

# Then we test case the removal of the visitor
museum.unregister_visitor(visitor)

# We then verify the visitor is no longer registered
assert visitor not in museum._visitors, "Visitor was not successfully deregistered."
print(f"{visitor} was successfully unregistered from the museum.")

# When the adult price of the ticket is 63 AED and VAT is 5%
visitor = Visitor("V003", "Bassem", "Rashed", 32, "Single", "853958596363")
ticket = Ticket(visitor, TypeOfVisit.INDIVIDUAL, originalPrice=63.0)

final_price = ticket.calculatePriceForOne()  # Calculates the price including VAT

expected_price = 63.0 * (1 + Ticket.VAT)  # Calculate expected price with VAT
print(final_price, expected_price)
print(
    " Ticket price for an individual visit calculated correctly with VAT by verfying the final price and expected price match")







