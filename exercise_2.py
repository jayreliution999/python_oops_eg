class Category:
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.no_of_product = 0
        self.parent = parent
        self.display_name = self.name

        # Change
        self.display_name1()
        # Change

    def display_category(self):
        print("CategoryName : ", self.name)
        print("CategoryCode : ", self.code)
        print("dispaly_name : ", self.display_name)
        print("no of products:", self.no_of_product)
        print("ParentCategory : ", self.parent)
        print("\n")

    def display_name1(self):
        count = self
        while (count.parent != None):
            #if self.parent:
                #print("Parent", self.parent)
                count.display_name = f'{count.parent.name} > {count.display_name}'
                #print("display_name", self.display_name)
                count = count.parent


class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        category.no_of_product = category.no_of_product + 1
        self.price = price

    def display_product(self):
        print("ProductName : ", self.name)
        print("ProductCode : ", self.code)
        print("Category : ", self.category.name)
        print("Price : ", self.price)
        print("\n")


#Parent Object

plastic = Category("plastic", 1)
chocolate = Category("chocolate", 2)
vehicle = Category("vehicle", 3)
electric = Category("electric", 4)
chemical = Category("chemical", 5)

#Child Object

c1 = Category("Tupperwere", 1, plastic)
c2 = Category("Dark Chocolate", 2, chocolate)
c3 = Category("Four Wheelers", 3, vehicle)
c4 = Category("DC", 4, electric)
c5 = Category("Paint", 5, chemical)

#Child of Child Object

childofc1 = Category("Water container", 1, c1)
childofc2 = Category("Amul", 2, c2)
childofc3 = Category("Audi", 3, c3)

#List of Products

# pro1 = Product("Milk bottle", 1, plastic, 225)
# pro2 = Product("Lily’s Dark", 2, chocolate, 100)
# pro3 = Product("Audi Q3", 3, vehicle, 1200000)
# pro4 = Product("Lindt Dark", 2, chocolate, 400)
#
# pro5 = Product("Wet food storage", 1, plastic, 300)
# pro6 = Product("Audi A8", 3, vehicle, 2500000)
# pro7 = Product("Hu Simple Dark", 2, chocolate, 500)
# pro8 = Product("Audi Q8", 3, vehicle, 3500000)
#
# pro9 = Product("Kitchen helper", 1, plastic, 3000)
# pro10 = Product("Audi A6", 3, vehicle, 4500000)
# pro11 = Product("Chocolove Dark", 2, chocolate, 600)
# pro12 = Product("Freezer Storage", 1, plastic, 450)
#
# pro13 = Product("Fan", 4, electric, 1250)
# pro14 = Product("TubeLight", 4, electric, 45)
#
# pro15 = Product("Asian Paint", 5, chemical, 850)
# pro16 = Product("Dulux Paint", 5, chemical, 650)

pro1 = Product("Milk bottle", 1, c1, 225)
pro2 = Product("Lily’s Dark", 2, c2, 100)
pro3 = Product("Audi Q3", 3, c3, 1200000)
pro4 = Product("Lindt Dark", 2, c2, 400)

pro5 = Product("Wet food storage", 1, c1, 300)
pro6 = Product("Audi A8", 3, c3, 2500000)
pro7 = Product("Hu Simple Dark", 2, c2, 500)
pro8 = Product("Audi Q8", 3, c3, 3500000)

pro9 = Product("Kitchen helper", 1, c1, 3000)
pro10 = Product("Audi A6", 3, c3, 4500000)
pro11 = Product("Chocolove Dark", 2, chocolate, 600)
pro12 = Product("Freezer Storage", 1, plastic, 450)

pro13 = Product("Fan", 4, electric, 1250)
pro14 = Product("TubeLight", 4, electric, 45)

pro15 = Product("Asian Paint", 5, chemical, 850)
pro16 = Product("Dulux Paint", 5, chemical, 650)


#c1.display_name1()
# c2.display_name1()
# c3.display_name1()
# c4.display_name1()
# c5.display_name1()


c1.display_category()
c2.display_category()
c3.display_category()
c4.display_category()
c5.display_category()

# childofc1.display_category()
# childofc2.display_category()
# childofc3.display_category()
#
#childofc1.display_name1()
# childofc2.display_name1()
# childofc3.display_name1()

plastic.display_category()
chocolate.display_category()
vehicle.display_category()
electric.display_category()
chemical.display_category()

pro1.display_product()
pro2.display_product()
pro3.display_product()
pro4.display_product()
pro5.display_product()
pro6.display_product()
pro7.display_product()
pro8.display_product()
pro9.display_product()
pro10.display_product()
pro11.display_product()
pro12.display_product()
pro13.display_product()
pro14.display_product()
pro15.display_product()
pro16.display_product()






