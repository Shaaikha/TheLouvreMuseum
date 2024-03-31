
class Artifacts(ArtWork):
  """Creating class for the artworks found in the Musuem"""
  #Adding class constructor to add the attributes for the artwork found in the musuem successfully
  def __init__(self, yearFound="", description=""): #By adding self keyword we will initialize object of the class
   super().__init__(title, artist, dateOfCreation,  historicalSignificance, location) #By using the super() function it will pass the attributes of the parent class of Artworks
   self.__yearFound= yearFound
   self.__description= description


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
   self.caringMethod = newMethod  #Change the caring method
   print(f"New Caring method for '{self.title}': {self.caringMethod}")

 #For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
  def __str__(self):
   return super().__str__()+ f"Artifacts(Artifact Year Found: {self.__yearFound} Description of Artifact: {self.__description})"
