import csv 
import uuid
from datetime import datetime 

PATH = "/home/dev/workspace/projects/pos-system/db/order.csv"
FIELDNAMES = []


class Order:
    def __init__(self, customer_id, sold_product, total_order_amount, payment): 
        self.id = uuid.uuid4()
        self.date = datetime.now()
        self.customer_id = customer_id
        self.sold_product = sold_product
        self.total_order_amount = total_order_amount
        self.payment = payment

        