class SecuritySystem:
    """Creating class for the security system found in the Musuem"""

    # Adding class constructor to add the attributes for the security found in the musuem successfully
    def __init__(self, securityID="", numOfCameras=0, alarms=0, viwInDark="",
                 securityCode=""):  # By adding self keyword we will initialize object of the class
        self.__securityID = securityID
        self.__numOfCameras = numOfCameras
        self.__alarms = alarms
        self.__viewInDark = viwInDark
        self.__securityCode = securityCode

        # Getters

    def getSecurityID(self):
        # Getter for securityID
        return self._securityID

    def getNumOfCameras(self):
        # Getter for numOfCameras
        return self._numOfCameras

    def getAlarms(self):
        # Getter for alarms
        return self._alarms

    def getViewInDark(self):
        # Getter for viewInDark
        return self._viewInDark

    def getSecurityCode(self):
        # Getter for securityCode
        return self._securityCode

    # Setters
    def setSecurityID(self, securityID=""):
        # Setter for securityID
        self._securityID = securityID

    def setNumOfCameras(self, numOfCameras=0):
        # Setter for numOfCameras
        self._numOfCameras = numOfCameras

    def setAlarms(self, alarms=0):
        # Setter for alarms
        self._alarms = alarms

    def setViewInDark(self, viewInDark=""):
        # Setter for viewInDark
        self._viewInDark = viewInDark

    def setSecurityCode(self, securityCode=""):
        # Setter for securityCode
        self._securityCode = securityCode

    def detectStealing(self, detectStealing):
        # Creating a function the will detect stealing at the louvre
        print("Detecting stealing sensor is activated")

    def countVisitors(self, countVisitors):
        # Creating a function the will count the total visitors at the louvre
        print("Detecting the count of visitors is activated")

    def storeVisitorData(self, storeVisitorData):
        # Creating a function the will store data of the visitors at the louvre
        print("Storage of visitor data system is applied")

    # For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
        return f"SecuritySystem(Security ID: {self.__securityID}, Number of Camera: {self.__numOfCameras}, Alarms:{self.__alarms} , Camera View in the Dark: {self.__viewInDark}, Security Passcode: {self.__securityCode})"

