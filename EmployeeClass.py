class Employee:
    """Creating class for the louvre musuem employees"""

    # Adding class constructor to add the attributes for the musuem successfully
    def __init__(self, employeeID="", workingHours="", firstName="", lastName="",
                 nationality=""):  # By adding self keyword we will initialize object of the class
        self.__employeeID = employeeID
        self.__workingHours = workingHours
        self.__firstName = firstName
        self.__lastName = lastName
        self.__nationality = nationality

        # Getter for employeeID

    def getEmployeeID(self):
        # getter for employeeID
        return self.__employeeID

    # Setter for employeeID
    def setEmployeeID(self, employeeID=""):
        # setter for employeeID
        self.__employeeID = employeeID

    # Getter for workingHours
    def getWorkingHours(self):
        # getter for workingHours
        return self.__workingHours

    # Setter for workingHours
    def setWorkingHours(self, workingHours=""):
        # setter for workingHours
        self.__workingHours = workingHours

    # Getter for firstName
    def getFirstName(self):
        # getter for firstName
        return self.__firstName

    # Setter for firstName
    def setFirstName(self, firstName=""):
        # setter for firstName
        self.__firstName = firstName

    # Getter for lastName
    def getLastName(self):
        # getter for lastName
        return self.__lastName

    # Setter for lastName
    def setLastName(self, lastName=""):
        # setter for lastName
        self.__lastName = lastName

    # Getter for nationality
    def getNationality(self):
        # getter for nationality
        return self.__nationality

    # Setter for nationality
    def setNationality(self, nationality=""):
        # setter for nationality
        self.__nationality = nationality

    def calculateSalary(self, hourWage):
        # Creating a function the will calculate employee salary using exception handling try and except
        try:
            salary = int(self.workingHours) * hourWage
            print(f"Total Salary for {self.__firstName} {self.__lastName}: {salary}")
        except ValueError:
            print("Your input for working hours is invalid")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"Employee(ID: {self.__employeeID} Working Hours: {self.__workingHours}, Name:{self.__firstName} {self.__lastName}, Employee Nationality: {self.__nationality})"

