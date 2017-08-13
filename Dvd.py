
import sys, datetime
from AbstractItem import AbstractItem

class Dvd(AbstractItem):
  NUMBER_OF_DAYS = 5
  DELAY_VALUE = 100
  RENTAL_COST = 350

  def __init__(self, title, genre, barcode):
    super(Dvd, self).__init__(title, genre, barcode)


  def setRented(self, today):
    self.rented = True
    self.dueDate = today + datetime.timedelta(days=self.NUMBER_OF_DAYS)

  def setReturned(self, today):
    self.rented = False
    self.dueDate = None

  def getRentalCost(self):
    return self.RENTAL_COST