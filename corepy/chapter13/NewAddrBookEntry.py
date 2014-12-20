
import Name 
import Phone

class NewAddrBookEntry(object):
	def __init__(self, nm, pn):
		self.name = Name.Name(nm)
		self.phone = Phone.Phone(pn)
		print "Create a book entry for ",self.name.toString()


be = NewAddrBookEntry("vonzhou", "4352345235")
