#!/usr/bin/env python
# coding: UTF-8
#
## @package AbstractItem
#
#  Partial implementation of the Item interface.
#
#  @author Paulo Roma
#  @since 11/07/2017

import Item, sys

##
#  Partial implementation of the Item interface.
#
class AbstractItem(Item.Item):

	##
	#  Constructs a new Item with the given title, genre, and barcode.
	#  This constructor may only be invoked by subclasses.
	#  @param title the title of the item
	#  @param genre the genre of the item
	#  @param barcode a unique integer identifier for the item
	#
	def __init__(self, title, genre, barcode):
		##  Title of this item.
		self.__title   = title
		##  Genre of this item.
		self.__genre   = genre
		##  Unique Barcode for this item.
		self.__barcode = barcode
		##  Rental status of this item.
		self.__rented  = False
		##  Due date for this item.
		self.__dueDate = None

	## Returns whether this item is rented.
	def isRented(self):
		return self.__rented

	## Returns this item due date.
	def getDueDate(self):
		if (self.rented):
			return self.__dueDate
		return None

	## Returns this item title.
	def getTitle(self):
		return self.__title

	## Returns this item barcode.
	def getBarcode(self):
		return self.__barcode


	def setRented(self, today):
		pass
	##
	#  Returns a representation of the state of this object as a
	#  multiline string.  The format is:
	#  <pre>
	#    type
	#    title
	#    (genre)
	#    status
	#  </pre>
	#  The status is either
	#  <pre>
	#    Rented: yyyy-mm-dd
	#  </pre>
	#  or
	#  <pre>
	#    Available
	#  </pre>
	#  where "yyyy-mm-dd" is the current due date.
	#
	#  @return a string representation of this object
	#
	def __str__(self):
		s = type(self).__name__ + "\n"
		s += self.getTitle() + "\n"
		s += " (" + self.getGenre() + ")\n"
		if self.isRented():
			s += "Rented: " + self.getDueDate()
		else:
			s += "Available"
		return s

	##
	#  Determines whether this item is the same as another
	#  one based on its barcode.
	#  @param obj
	#     the object to compare to this item
	#  @return
	#     true if the given object is an AbstractItem
	#     with the same barcode as this one
	#
	def __eq__(self, obj):
		if not isinstance(obj,AbstractItem):
			return false
		return self.getBarcode() == obj.getBarcode()

def main():
	item1 = AbstractItem("A Movie Name", "Action", 1)
	item2 = AbstractItem("Another Movie Name", "Action", 2)
	#item1.setReturned()
	print (item1 == item2)
	print (item1)
	print (item2)

# if __name__=="__main__":
#     sys.exit(main())
