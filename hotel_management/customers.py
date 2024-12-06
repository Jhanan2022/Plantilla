class Customer:
    def __init__(self, customer_id: int, customer_name: str, customer_email: str):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_email = customer_email

class CustomerManagement:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer: Customer):
        self.customers[customer.customer_id] = {
            "customer_name": customer.customer_name,
            "customer_email": customer.customer_email,
        }
        print(f"Cliente {customer.customer_name} creado con éxito.")

    def get_customer(self, customer_id: int):
       customer = self.customers.get(customer_id)
       if customer:
           print(f"Nombre: {customer['customer_name']} - Email: {customer['customer_email']}.")
       else:
           print(f"Cliente con el ID {customer_id} no encontrado.")

if __name__ == "__main__":
    customer_mgmt = CustomerManagement()
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer_mgmt.add_customer(customer1)
    customer_mgmt.get_customer(1)