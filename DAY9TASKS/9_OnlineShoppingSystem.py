class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, warranty, brand):
        super().__init__(name, price, warranty)
        self.brand = brand

    def display(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Warranty:", self.warranty)
        print("Brand:", self.brand)
m1 = MobilePhone("Smartphone", 20000, "1 Year", "Samsung")
m1.display()
