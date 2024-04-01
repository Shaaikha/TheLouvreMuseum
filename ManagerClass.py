from EmployeeClass import Employee
# Class for enumrating the departements the managers work for
from enum import Enum
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
