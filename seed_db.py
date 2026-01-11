import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_backend_graphql_crm.settings')
django.setup()

from crm.models import Customer, Product

def run():
    Customer.objects.all().delete()
    Product.objects.all().delete()

    customers = [
        {"name": "Kaleab", "email": "kaleab@gmail.com", "phone": "+2514567890"},
        {"name": "Matiwos", "email": "mati00@gmail.com", "phone": "123-456-7890"},
        {"name": "tuti", "email": "tuti@yahoo.com"}
    ]
    for c in customers:
        Customer.objects.create(**c)

    products = [
        {"name": "Laptop", "price": 999.99, "stock": 10},
        {"name": "Phone", "price": 499.99, "stock": 20},
        {"name": "Tablet", "price": 299.99, "stock": 15}
    ]
    for p in products:
        Product.objects.create(**p)

    print("Database seeded successfully!!")

if __name__ == "__main__":
    run()
