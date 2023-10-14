import uuid
import json

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


