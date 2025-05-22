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

class CartDBStorage:
    def __init__(self,cart):
        self.cart=cart
    
    def savetoDB(self):
        print("Saving to DB")


        
cart = ShpopingCart()
cart.add_product(Product("Laptop", 50000))
cart.add_product(Product("Mobile", 20000))
cart.add_product(Product("Tablet", 10000))

invoice = Invoice_Print(cart)
invoice.print_invoice(

)

cartDB = CartDBStorage(cart)
cartDB.savetoDB(
)