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

#List of Products

category_list = [plastic, chocolate, vehicle, c1, c2, c3, c4, c5, childofc1, childofc2, childofc3, electric, chemical]


product_list = [
    Product("Water bottle", c1, 225),
    Product("Lily’s Dark", c2, 100),
    Product("Audi Q3", c3, 1200000),
    Product("Lindt Dark", c2, 400),
    Product("Wet food storage", c1, 300),
    Product("Audi A8", c3, 2500000),
    Product("Hu Simple Dark", c2, 500),
    Product("Audi Q8", c3, 3500000),
    Product("Kitchen helper", c1, 3000),
    Product("Audi A6", c3, 4500000),
    Product("Chocolove Dark", c2, 600),
    Product("Freezer Storage", c1, 450),
    Product("Fan", c4, 4500),
    Product("i20", vehicle, 340000),
    Product("Fruit & Nuts", chocolate, 340),
    Product("Light & series", electric, 940),
    Product("Tubelight", electric, 125),
    Product("Asian Paint", chemical, 3000),
    Product("Dulux Paint", chemical, 2500),
    Product("Super Paint", chemical, 1000),
]

for category in category_list:
    category.display_category()
for product in product_list:
    product.display_product()

