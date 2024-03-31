#Class for enumrating the departements the managers work for
from enum import Enum
class ManagerDep(Enum):
    IT = "IT Departement"
    MARKETING = "Marketing Departement"
    FINANCE= "Finanace Departement"

class Manager(Employee):
  """Creating class for the managers found in the Musuem"""
  #Adding class constructor to add the attributes for the managers working in the musuem successfully
  def __init__(self, departement=ManagerDep.IT, yearsOfWorking=0): #By adding self keyword we will initialize object of the class
   super().__init__(employeeID="", workingHours="", firstName="", lastName="", nationality="") #By using the super() function it will pass the attributes of the parent class of Artworks
   self._departement= departement
   self._yearsOfWorking= yearsOfWorking

   # Getters
  def getDepartment(self):
        # getter for department
        return self._department

  def getYearsOfWorking(self):
        # getter for yearsOfWorking
        return self._yearsOfWorking

  def getIsActive(self):
        # getter for isActive
        return self._isActive

  def getBonus(self):
        # getter for bonus
        return self._bonus

    # Setters
  def setDepartment(self, department=ManagerDep.IT):
        # setter for department
        self._department = department

  def setYearsOfWorking(self, yearsOfWorking=''):
        # setter for yearsOfWorking
        self._yearsOfWorking = yearsOfWorking


  def fireManager(self, fireManager):
 # Creating a function to fire a manager at the louvre
        self.__isActive = False
        print(f"Manager {self.__firstName} {self.__lastName} has been fired.")

  def addBonus(self, bonusAmount):
#Creating a function to add bonus to the manager based on success
        self.__bonus += bonusAmount
        print(f"Manager {self.__firstName} {self.__lastName} gets bonus equals to {bonusAmount}. Overall bonus: {self.__bonus}")

 #For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
  def __str__(self):
    return super().__str__()+ f"Manager(Manager Departement: {self.__departement.value} ,Years Of Working {self.__yearsOfWorking})"
