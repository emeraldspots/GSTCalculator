## Author: Arundhati Saha
## Modified: 17.09.2021
## GST Calculator
import sys

## List of commodities in each product categories 
foodGrainsList = ["Rice","Wheat","Dal"] 
furnitureList = ["Table","Sofa","Chair"]
electronicsList = ["Mobile","TV","Tablet"]
cosmeticsList = ["Cream","Perfume","Lotion"]

class GST:
	def __init__(self,unit,initialUnitPrice,tax):
		self.unit = unit
		self.initialUnitPrice = initialUnitPrice
		self.tax = tax
	def getGST(self): ## Calculates gst amount per unit
		self.gstPerUnit =  round(self.tax*self.initialUnitPrice,2) ## Assuming that printing until 2 decimal point is allowed
		return self.gstPerUnit
	def getFinalPrice(self): ## Calculates final price of commodity after GST
		return round((self.gstPerUnit+self.initialUnitPrice)*self.unit,2) ## Assuming that printing until 2 decimal point is allowed
## Subclasses based on product categories
class foodGrains(GST):
	tax = 0
	def __init__(self,unit,initialUnitPrice):
		super().__init__(unit,initialUnitPrice,foodGrains.tax)
class furniture(GST):
	tax = 0.05
	def __init__(self,unit,initialUnitPrice):
		super().__init__(unit,initialUnitPrice,furniture.tax)
class electronics(GST):
	tax = 0.18
	def __init__(self,unit,initialUnitPrice):
		super().__init__(unit,initialUnitPrice,electronics.tax)
class cosmetics(GST):
	tax = 0.28
	def __init__(self,unit,initialUnitPrice):
		super().__init__(unit,initialUnitPrice,cosmetics.tax)

## Processing Output		
for line in sys.stdin:
	try:
		unit,commodity,initialUnitPrice = line.rstrip().split(' ')
		unit = int(unit)
		initialUnitPrice = int(initialUnitPrice)
	except ValueError as ve:
		print("Input Values are in incorrect format:",ve)
		continue ## Application will still return result for those inputs entered correctly
	if commodity in foodGrainsList:
		GSTObj = foodGrains(unit,initialUnitPrice)
	elif commodity in furnitureList:
		GSTObj = furniture(unit,initialUnitPrice)
	elif commodity in electronicsList:
		GSTObj = electronics(unit,initialUnitPrice)
	elif commodity in cosmeticsList:
		GSTObj = cosmetics(unit,initialUnitPrice)
	else:
		print("Commodity not listed in given Product Categories")
		continue
	print(GSTObj.getGST(),GSTObj.getFinalPrice())