from exercise_2 import Product
from exercise_2 import Category


class Location:

    code_location = 0

    def __init__(self, name):
        self.name = name
        self.code = Location.code_location + 1
        Location.code_location = Location.code_location + 1

    def display_1(self):
        print("----------------------------")
        print("Location Name : ", self.name)
        print("Location Code : ", self.code)
        print("----------------------------")


class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        self.display = f'quantity of product : {self.quantity} from {self.from_location.name} to {self.to_location.name}'

        try:
            print('\nproduct_name:', product.name, '\nFrom_location: ->', self.from_location.name, 'To_location: ->',
                self.to_location.name, 'quantity: ->', self.quantity)
            if self.from_location in self.product.stock_at_location:

                if self.product.stock_at_location[self.from_location] >= self.quantity:  # 40 >=10    for soap
                    qun = self.product.stock_at_location[self.from_location] - self.quantity  # 40-10=30
                    self.product.stock_at_location.update({self.from_location: qun})  # {rajkot,30}
                    if self.to_location in self.product.stock_at_location:  # {ahemdabad}it check location is available or not
                        qun1 = self.product.stock_at_location[self.to_location] + self.quantity  # 10+30
                        self.product.stock_at_location.update({self.to_location: qun1})  # {ahemdabad,40}
                        # print(self.product.name,"stock added")
                    else:
                         # if not available location it add both location and quantity
                        self.product.stock_at_location.update({self.to_location: self.quantity})

                    # print(self.product.name,"done movement")
                    self.display = f'product quantity :{self.quantity} from {self.from_location.name} to {self.to_location.name}'

                else:
                    print(f"quantity no: {self.quantity} of {self.product.name} not available {self.from_location.name}")

        except Exception:
            print("no location for that product\n")

    @staticmethod
    def movements_by_product(product):
        flag = 0
        for item in listof_movement:
            if item.product.name == product.name:
                flag = 1
                print(item.display)
        if flag == 0:
            print("No Movement of product")


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

soap = Product("Soap", chemical, 100, {rajkot: 40, ahemdabad: 30, baroda: 10})
detergent = Product("Detergent", chemical, 75, {ahemdabad: 10, surat: 20, baroda: 40})
toothpaste = Product("Toothpaste", chemical, 45, {rajkot: 50, baroda: 30, ahemdabad: 20})
chalk = Product("Chalk", chemical, 65, {surat: 30, rajkot: 10, ahemdabad: 40})
marble = Product("Marble", chemical, 50, {baroda: 25, rajkot: 30, surat: 20})

listof_product = [soap, detergent, toothpaste, chalk, marble]

for i in listof_product:
    print(i.name) #name of product
    for j in i.stock_at_location: #print dictionary of location name,quntity value
        print(f'{j.name} -> {i.stock_at_location[j]}')
    print()


#Move 5 Products from one location to another location

movement1 = Movement(rajkot, ahemdabad, soap, 10)
movement2 = Movement(rajkot, surat, detergent, 5)
movement3 = Movement(ahemdabad, baroda, toothpaste, 25)
movement4 = Movement(baroda, surat, chalk, 4)
movement5 = Movement(ahemdabad, surat, marble, 100)

listof_movement = [movement1, movement2, movement3, movement4, movement5]

for i in listof_product:
    print(i.name) #name of product
    Movement.movements_by_product(i) #Movement of Product
print()

print("---------------------------")
print("Stock at location with product details")
print("---------------------------")
for i in listof_product:
    i.display_product()
    print("Location of Product : ")
    for j in i.stock_at_location:
        print(f'{j.name} -> {i.stock_at_location[j]}')
    print()

print("----------------------------")
print("product list by location : ")
print("----------------------------")
for i in listof_location:
    print(i.name)
    for lp in listof_product:
        if i in lp.stock_at_location:
            print(f'{lp.name} -> {lp.stock_at_location[i]}')
    print()

