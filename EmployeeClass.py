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