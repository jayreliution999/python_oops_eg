from exercise_2 import Product
from exercise_2 import Category


class Location:

    code_location = 0

    def __init__(self, name):
        self.name = name
        self.code = Location.code_location + 1
        Location.code_location = Location.code_location + 1

    def display_1(self):
        print("Location Name : ", self.name)
        print("Location Code : ", self.code)


class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

    def display_movement(self):
        print("FromLocation : ", self.from_location)
        print("To Location : ", self.to_location)
        print("Product Name :", self.product)
        print("How many Quantity : ", self.quantity)

    @staticmethod
    def movements_by_product(product):
        pass

#Location of object

rajkot = Location("Rajkot")
ahemdabad = Location("Ahemdabad")
baroda = Location("Baroda")
surat = Location("Surat")

listof_location = [rajkot, ahemdabad, baroda, surat]
for i in listof_location:
    i.display_1()

#Products Object

chemical = Category("Chemical")

soap = Product("Soap", chemical, 100, {rajkot: 40, ahemdabad: 20, baroda: 10})
detergent = Product("Detergent", chemical, 75, {ahemdabad: 10, surat: 20, baroda: 40})
toothpaste = Product("Toothpaste", chemical, 45, {rajkot: 50, baroda: 30, ahemdabad: 20})
chalk = Product("Chalk", chemical, 65, {surat: 30, rajkot: 10, ahemdabad: 40})
marble = Product("Marble", chemical, 50, {baroda: 25, rajkot: 30, surat: 20})

listof_product = [soap, detergent, toothpaste, chalk, marble]
for i in listof_product:
    print(i.name)
    for j in i.stock_at_location: #print dictionary of location name,quntity value
        print(f'{j.name} -> {i.stock_at_location[j]}')



#Move 5 Products from one location to another location

movement1 = Movement(rajkot, ahemdabad, soap, 10)
movement2 = Movement(rajkot, surat, detergent, 5)
movement3 = Movement(ahemdabad, baroda, toothpaste, 25)
movement4 = Movement(baroda, surat, chalk, 4)
movement5 = Movement(ahemdabad, surat, marble, 0)



