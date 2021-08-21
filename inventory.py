from product import Product

class Inventory():
    def __init__(self):
        self.products=[]
        
    def addProducts(self, i):
            self.products.append(i)
            
    def getProducts(self):
        return self.products
    
    def getProduct_ID(self, id):
        reqProduct=None
        for i in self.products:
            if i.prod_id==id:
                reqProduct=i
                break
        return reqProduct
    
    