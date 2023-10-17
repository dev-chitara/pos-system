import csv 
import uuid
from datetime import datetime 
from inventory_management_system.schemas.products import get_product

PATH = "/home/dev/workspace/projects/pos-system/db/order.csv"
FIELDNAMES = []


class Order:
    def __init__(self, customer_id, product_id, payment_type): 
        self.id = uuid.uuid4()
        self.date = datetime.now()
        self.customer_id = customer_id
        self.product_id = product_id
        self.sold_product = {}
        self.total_order_amount = 0
        if type(payment_type) == None:
            self.payment_type = "cash"
        else:
            self.payment_type = payment_type

    def set_sold_product(self,sold_quanity):
        self.sold_product["product_id"] = self.product_id
        self.sold_product["sold_quanity"] = sold_quanity
        product_dict = get_product(self.sold_product.get(self.product_id))
        self.sold_product["total_amount"] = product_dict["price"]*self.sold_product.get(sold_quanity)
    
    def set_total_order_amonut(self):
        self.total_order_amount  = self.sold_product["total_amount"]









    