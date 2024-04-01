from EmployeeClass import Employee
class TourGuide(Employee):
  """Creating class for the Tour Guide working in the Musuem"""
  #Adding class constructor to add the attributes for the managers working in the musuem successfully
  def __init__(self, numOfPeople=0, groupID="", dateOfTour=""): #By adding self keyword we will initialize object of the class
    super().__init__(employeeID="", workingHours="", firstName="", lastName="", nationality="") #By using the super() function it will pass the attributes of the parent class of Artworks
    self.__numOfPeople= numOfPeople
    self.__groupID= groupID
    self.__dateOfTour= dateOfTour

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
   print(f"Backup guide will take place of the main tour guide {backupGuide.firstName} {backupGuide.lastName} for date {self.__dateOfTour}.")

 #For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
  def __str__(self):
   return super().__str__()+ f"TourGuide(People need Guidance: {self.__numOfPeople} , Group ID {self.__groupID}, Date of the Tour{self.__dateOfTour})"
