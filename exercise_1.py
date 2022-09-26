class Category:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_product = 0

    def display_category(self):
        print("CategoryName : ", self.name)
        print("CategoryCode : ", self.code)
        print("No of product : ", self.no_of_product)
        print("\n")


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


cat1 = Category("PLASTIC", 1)
cat2 = Category("CHEMICAL", 2)
cat3 = Category("ELECTRONICS", 3)


pro1 = Product("Tupperwere", 1, cat1, 1000)
pro2 = Product("Era", 1, cat1, 3300)
pro3 = Product("Plastoranger", 1, cat1, 2250)

pro4 = Product("dove", 2, cat2, 86)
pro5 = Product("lux", 2, cat2, 54)
pro6 = Product("Dettol", 2, cat2, 120)

pro7 = Product("LG", 3, cat3, 16000)
pro8 = Product("Samsung", 3, cat3, 16500)
pro9 = Product("Sony", 3, cat3, 19000)
pro10 = Product("Dell", 3, cat3, 33000)

cat1.display_category()
cat2.display_category()
cat3.display_category()

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
