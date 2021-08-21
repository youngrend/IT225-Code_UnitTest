from product import Product
from sale_prod import Sale_Prod


class Sale():
    def __init__(self):
        self.sale_items=[]
        
    def addSale_Items(self, sale_item):
        self.sale_items.append(sale_item)
        
    def getSale_Items(self):
        return self.sale_items
    
    
    
    