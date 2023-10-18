from pos_system.schemas.customers import get_customers, create_customers, get_customer, update_customer, delete_customer
from pos_system.schemas.orders import get_orders,create_order,get_order

# create_customers("Harshit", 9882686578)
# create_customers("Harsh", 7612576893)
# create_customers("Mohit", 9774214672)
# create_customers("Rahul", 7834791814)
# create_customers("Dev", 8941626486)
# create_customers("Sanjay", 1298126825)


# print(get_customers())

# print(get_customer("ae90a69c-db75-461b-8bd4-f3130bfe83ce"))

# print(update_customer("ae90a69c-db75-461b-8bd4-f3130bfe83ce", "Vinod", 8635268631))

# print(delete_customer("1827c35e-6581-48e7-b4f7-ca821e1689b5"))



def main():
    create_order("fbac7c1f-9712-4867-a6e9-9e180228e5ac", "5681e482-51e7-4f37-84bb-7e6de1888d0a", "UPI", 4) 

  
main()