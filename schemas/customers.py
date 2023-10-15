import csv
import uuid


PATH = "/home/dev/workspace/projects/pos-system/db/customers.csv"
FIELDNAMES = ["id", "name", "contact_number"]

class Customer:
    def __init__(self, name, contact_number):
        self.id = uuid.uuid4()
        self.name = name
        self.contact_number = contact_number

    
    def _validation(self, data):
        valid_type = {
            "name": str,
            "contact_number": int
        }

        for item in data:
            if type(data.get(item)) != valid_type.get(item):
                return f"Cannot set invalid value :{item}"
            
            elif data.get(item):
                return f"Cannot set an empty value :{item}"
            

    def set_customers(self, **kwargs):
        invalid = self._validation(kwargs)

        if invalid:
            return invalid
        
        self.name = kwargs.get("name", self.name)
        self.contact_number = kwargs.get("contact_number", self.contact_number)


    def get_customer_details(self):
        return self.__dict__


def get_customers():
    with open(PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        for item in reader:
            records.append(item)
        return records


def create_customers(name, contact_number):
    customer = Customer(name, contact_number)
    customer_dict = customer.get_customer_details()

    with open(PATH, "a") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow(customer_dict)


def get_customer(id):
    with open(PATH, "r") as file:
        reader = csv.DictReader(file)

        for item in reader:
            if item["id"] == id:
                return item


def update_customer(id, name, contact_number):
   with open(PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        is_exists = False

        for item in reader:
            if item["id"] == id:
                item["name"] = name
                item["contact_number"] = contact_number
                is_exists = True
            records.append(item)

        if is_exists:
            with open(PATH, "w") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(records)
                
        else:
            return (is_exists, "Customer does not exists")
        
        return (is_exists, "Successfully updated")


def delete_customer(id):
   with open(PATH, "r") as file:
        reader = csv.DictReader(file)

        records = []
        is_exists = False

        for item in reader:
            if item["id"] != id:
                is_exists = True
                records.append(item)

        if is_exists:
            with open(PATH, "w") as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(records)
                
        else:
            return (is_exists, "Customer does not exists")
        
        return (is_exists, "Successfully deleted")
