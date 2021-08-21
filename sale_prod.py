from product import Product

class Sale_Prod():
    def __init__(self, prod, quantity):
        self.prod=prod
        self.quantity=quantity
        
    def getProd(self):
        return self.prod
    
    def getQuantity(self):
        return self.quantity
    