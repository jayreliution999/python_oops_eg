class Category:
    code = 0
    def __init__(self, name, parent=None):
        self.name = name
        self.code = Category.code + 1
        Category.code = Category.code + 1
        self.no_of_product = 0
        self.product = []
        self.parent = parent
        self.display_name = self.name
        self.display_name1()

    def display_category(self):
        print("CategoryName : ", self.name)
        print("CategoryCode : ", self.code)
        print("dispaly_name : ", self.display_name)
        print("no of products:", self.no_of_product)
        print("Name of all Products : ", self.product)
        print()

    def display_name1(self):
        count = self
        while (count.parent != None):
                self.display_name = f'{count.parent.name} > {self.display_name}'
                count = count.parent

class Product:
    codep = 0
    def __init__(self, name, category, price):
        self.name = name
        self.code = Product.codep + 1
        Product.codep = Product.codep + 1
        self.category = category.name
        self.no_of_product = self.code + 1
        category.no_of_product = category.no_of_product + 1
        self.price = price
        category.product.append(self.name)

    def display_product(self):
        print("ProductName : ", self.name)
        print("ProductCode : ", self.code)
        print("Category : ", self.category)
        print("Price : ", self.price)
        print("\n")


#Parent Object

plastic = Category("plastic")
chocolate = Category("chocolate")
vehicle = Category("vehicle")
electric = Category("electric")
chemical = Category("chemical")

#Child Object

c1 = Category("Tupperwere", plastic)
c2 = Category("Dark Chocolate", chocolate)
c3 = Category("Four Wheelers", vehicle)
c4 = Category("DC", electric)
c5 = Category("Paint", chemical)

#Child of Child Object

childofc1 = Category("Water container", c1)
childofc2 = Category("Amul", c2)
childofc3 = Category("Audi", c3)

#Name of All Products

pro1 = Product("Water bottle", c1, 225)
pro2 = Product("Lily’s Dark", c2, 100)
pro3 = Product("Audi Q3", c3, 1200000)
pro4 = Product("Lindt Dark", c2, 400)
pro5 = Product("Wet food storage", c1, 300)
pro6 = Product("Audi A8", c3, 2500000)
pro7 = Product("Hu Simple Dark", c2, 500)
pro8 = Product("Audi Q8", c3, 3500000)
pro9 = Product("Kitchen helper", c1, 3000)
pro10 = Product("Audi A6", c3, 4500000)
pro11 = Product("Chocolove Dark", c2, 600)
pro12 = Product("Freezer Storage", c1, 450)
pro13 = Product("Fan", c4, 4500)
pro14 = Product("i20", vehicle, 340000)
pro15 = Product("Fruit & Nuts", chocolate, 340)
pro16 = Product("Light & series", electric, 940)
pro17 = Product("Tubelight", electric, 125)
pro18 = Product("Asian Paint", chemical, 3000)
pro19 = Product("Dulux Paint", chemical, 2500)
pro20 = Product("Super Paint", chemical, 1000)

#List of category

category_list = [plastic, chocolate, vehicle, c1, c2, c3, c4, c5, childofc1, childofc2, childofc3, electric, chemical]

#List of product

product_list = [pro1, pro2, pro3, pro4, pro5, pro6, pro7, pro8, pro9, pro10, pro11, pro12, pro13, pro14, pro15,
                pro16, pro17, pro18, pro19, pro20]


for category in category_list:
    category.display_category()
for product in product_list:
    product.display_product()




