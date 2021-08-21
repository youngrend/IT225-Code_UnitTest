import unittest
from product import Product
from sale_prod import Sale_Prod
from sale import Sale
from inventory import Inventory

class ProductTest(unittest.TestCase):
    def setUp(self):
        self.product=Product(1, 'Lacroix', 'Fave Drink', 4.99)
        
    def test_prodString(self):
        self.assertEqual(str(self.product), self.product.prod_name)
        
    def test_getProd_Price(self):
        self.assertEqual(str(self.product.getProd_Price()), '4.99')
        
    def test_getProd_ID(self):
        self.assertEqual(str(self.product.getProd_ID()), '1')
        
    def test_getProd_Desc(self):
        self.assertEqual(str(self.product.getProd_Desc()), 'Fave Drink')
        
class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.product1=Product(1, 'Lacroix', 'Fave Drink', 4.99)
        self.product2=Product(2, 'Ruffles', 'Yum. Potatoe Chips', 3.75)
        self.product3=Product(3, 'Nurto Ultra', 'Dog Food', 15.99)
        
        self.inventory=Inventory()
        self.inventory.addProducts(self.product1)
        self.inventory.addProducts(self.product2)
        self.inventory.addProducts(self.product3)
        
    def test_getProducts(self):
        prod=self.inventory.getProducts()
        self.assertEqual(len(prod), 3)
        
    def test_getProduct_ID(self):
        prod_id=self.inventory.getProduct_ID(3)
        self.assertEqual(str(prod_id), 'Nutro Ultra')