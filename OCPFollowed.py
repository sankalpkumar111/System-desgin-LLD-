from abc import ABC ,abstractmethod
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class ShpopingCart:
    def __init__(self):
        self.products=[]
    
    def add_product(self,product):
        self.products.append(product)
    
    def get_product(self):
        return self.products

    def  toatlPrice(self):
        total=0
        for product in self.products:
            total+=product.price
        return total


class Invoice_Print:
    def __init__(self,invoice):
        self.invoice=invoice
    
    def print_invoice(self):
        print("Shoping cart Invoice")
        for product in self.invoice.get_product():
            print(f"{product.name} : {product.price}")
        
        print(f"Total RS: {self.invoice.toatlPrice()}")

class  Presitance:
    @abstractmethod
    def save(self ,cart: ShpopingCart):
        pass

class SaveToFile(Presitance):
    def save(self, cart:ShpopingCart):
        print("Saving to shoping cart to File..")

class SaveToSql(Presitance):
    def save(self, cart:ShpopingCart):
        print("Saving to shoping cart to Sql..")

class SaveToMongoDB(Presitance):
    def save(self, cart:ShpopingCart):
        print("Saving to shoping cart to MongoDB..")
    
cart=ShpopingCart()
cart.add_product(Product("Laptop", 50000))
cart.add_product(Product("Mobile", 20000))
cart.add_product(Product("Tablet", 10000))
cart.add_product(Product("Tablet", 10000))

printer=Invoice_Print(cart)
printer.print_invoice()

saveToFile=SaveToFile()
saveToFile.save(cart)

saveToSql=SaveToSql()
saveToSql.save(cart)

saveToMongoDB=SaveToMongoDB()
saveToMongoDB.save(cart)