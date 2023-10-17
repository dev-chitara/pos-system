import csv 
import uuid
from datetime import datetime 

PATH = "/home/dev/workspace/projects/pos-system/db/order.csv"
FIELDNAMES = []


class Order:
    def __init__(self, customer_id, sold_product, payment_type = "cash"): 
        self.id = uuid.uuid4()
        self.date = datetime.now()
        self.customer_id = customer_id
        self.sold_product = sold_product
        self.total_order_amount = 0
        self.payment_type = payment_type

    def set_sold_product(self, product_id, sold_quanity):
        self.sold_product = {}
        self.sold_product[f"{product_id}"] = sold_quanity







    