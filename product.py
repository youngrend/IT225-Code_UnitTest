class Product():
    
    def __init__(self, prod_id, prod_name, prod_desc, prod_price):
        self.prod_id=prod_id
        self.prod_name=prod_name
        self.prod_desc=prod_desc
        self.prod_price=prod_price
        
    def getProd_ID(self):
        return self.prod_id
    
    def getProd_Name(self):
        return self.prod_name
    
    def getProd_Desc(self):
        return self.prod_desc
    
    def getProd_Price(self):
        return self.prod_price
    
    def __str__(self):
        return self.prod_name