# import ENUM library for listing the limited options available
from enum import Enum


class GalleryLocation(Enum):
    PERMANENT = "permanent galleries"
    HALLS = "Exhibition halls"
    OUTDOOR = "Outdoor spaces"


class Gallery:
    """Creating class for the galleries in the Museum """

    # Adding class constructor to add the attributes for the exhibitions visited by visitors to enter the musuem successfully
    def __init__(self, galleryID="", galleryTitle="", featuredWork="", galleryTheme="", galleryDressCode="",
                 galleryLocation=GalleryLocation.PERMANENT):  # By adding self keyword we will initialize object of the class
        self._galleryID = galleryID
        self._galleryTitle = galleryTitle
        self._featuredWork = featuredWork
        self._galleryTheme = galleryTheme
        self._galleryDressCode = galleryDressCode
        self._galleryLocation = galleryLocation

        # Getters

    def getGalleryID(self):
        # Getter for galleryID
        return self._galleryID

    def getGalleryTitle(self):
        # Getter for galleryTitle
        return self._galleryTitle

    def getFeaturedWork(self):
        # Getter for featuredWork
        return self._featuredWork

    def getGalleryTheme(self):
        # Getter for galleryTheme
        return self._galleryTheme

    def getGalleryDressCode(self):
        # Getter for galleryDressCode
        return self._galleryDressCode

    def getGalleryLocation(self):
        # Getter for galleryLocation
        return self._galleryLocation

    # Setters
    def setGalleryID(self, galleryID=""):
        # Setter for galleryID
        self._galleryID = galleryID

    def setGalleryTitle(self, galleryTitle=""):
        # Setter for galleryTitle
        self._galleryTitle = galleryTitle

    def setFeaturedWork(self, featuredWork=""):
        # Setter for featuredWork
        self._featuredWork = featuredWork

    def setGalleryTheme(self, galleryTheme=""):
        # Setter for galleryTheme
        self._galleryTheme = galleryTheme

    def setGalleryDressCode(self, galleryDressCode=""):
        # Setter for galleryDressCode
        self._galleryDressCode = galleryDressCode

    def setGalleryLocation(self, galleryLocation=GalleryLocation.PERMANENT):
        # Setter for galleryLocation
        self._galleryLocation = galleryLocation

    def displayGalleryInfo(self, displayGalleryInfo):
        # Creating a function the will allow the displaying of the gellery details
        info = (
            f"Gallery ID: {self._galleryID}, "
            f"Title: {self._galleryTitle}, "
            f"Featured Work: {self._featuredWork}, "
            f"Theme: {self._galleryTheme}, "
            f"Dress Code: {self._galleryDressCode}, "
            f"Location: {self._galleryLocation.value}"
        )
        print(info)

    def updateTheme(self, updateTheme, newTheme):
        # This function is used to update the theme of the gallery
        self._galleryTheme = newTheme
        print(f"Updated Gallery Theme: {newTheme}")


#For the object to have clear and easy to read parameters, we will add __str__ function ensures proper object illustration
    def __str__(self):
      return f"Gallery(Gallery ID: {self._galleryID},Gallery Title: {self._galleryTitle}, Featured Work: {self._featuredWork} ,Gallery Theme: {self._galleryTheme}, Gallery Dress code: {self._galleryDressCode}, Gallery Location: {self._galleryLocation.value})"
