import csv 
import uuid
from datetime import datetime 
from inventory_management_system.schemas.products import get_product
from pos_system.schemas.customers import get_customer

PATH = "./pos_system/db/order.csv"
FIELDNAMES = ["id", "date", "customer_id", "sold_product", "product_id", "total_order_amount", "payment_type"]


class Order:
    def __init__(self, customer_id, product_id, payment_type = "cash"): 
        self.id = uuid.uuid4()
        self.date = datetime.now()
        self.customer_id = customer_id
        self.product_id = product_id
        self.sold_product = {}
        self.total_order_amount = 0
        self.payment_type = payment_type


    def set_sold_product(self,sold_quanity):
        self.sold_product["product_id"] = self.product_id
        self.sold_product["sold_quanity"] = sold_quanity
        product_dict = get_product(self.product_id)
        self.sold_product["total_amount"] = int(product_dict["price"])*self.sold_product["sold_quanity"]
    

    def set_total_order_amonut(self):
        self.total_order_amount = self.sold_product["total_amount"]


    def get_order_details(self):
        return self.__dict__
    

def get_orders():
    with open(PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        for item in reader:
            records.append(item)
        return records


def create_order(customer_id, product_id, payment_type , sold_quantity):
    order = Order(customer_id, product_id, payment_type)
    order.set_sold_product(sold_quantity)
    order.set_total_order_amonut()
    order_dict = order.get_order_details()

    with open(PATH, "a") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(order_dict)


def get_order(id):
    with open(PATH, "r") as file:
        reader = csv.DictReader(file)

        for item in reader:
            if item["id"] == id:
                return item


def generating_receipts(id):
    order_dict = get_order(id)
    customer_name = get_customer(order_dict["customer_id"])["name"]
    product_name = get_product(order_dict["product_id"])["name"]
    product_price = get_product(order_dict["product_id"])["price"]
    # product_quantity = order_dict["sold_product"]["sold_quanity"]
    total_order_amount = order_dict["total_order_amount"]
    print(f"Customer ID is :{order_dict['customer_id']}")
    print(f"Customer Name is :{customer_name}")
    print(f"Order Date is :{order_dict['date']}")
    print(f"Product Name is :{product_name}")
    print(f"Product Price is :{product_price}")
    # print(f"Product Quanity is :{product_quantity}")
    print(f"Total Order Amount is :{total_order_amount}")

    











    