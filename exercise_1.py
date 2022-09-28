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

    def __repr__(self):
        return '(product_name: {}, product_code: {}, product_cat: {},product_price:{}\n)'.format(self.name,
        self.code, self.category.name, self.price)

    def display_product(self):
        print("ProductName : ", self.name)
        print("ProductCode : ", self.code)
        print("Category : ", self.category.name)
        print("Price : ", self.price)
        print("\n")

    def price_sort_low_to_high(price_list):
        for i in range(0, len(price_list) - 1):
            for j in range(len(price_list) - 1):
                if (price_list[j].price > price_list[j+1].price):
                    price_list[j], price_list[j+1] = price_list[j+1], price_list[j]
        return print(price_list)

    def price_sort_high_to_low(price_list):
        for i in range(0, len(price_list) - 1):
            for j in range(len(price_list) - 1):
                if (price_list[j].price < price_list[j + 1].price):
                    price_list[j], price_list[j + 1] = price_list[j + 1], price_list[j]
        return print(price_list)


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

price_list = [pro1, pro2, pro3, pro4, pro5, pro6, pro7, pro8, pro9, pro10]

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

Product.price_sort_low_to_high(price_list)
Product.price_sort_high_to_low(price_list)
