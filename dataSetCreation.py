import random
import pandas as pd
from datetime import datetime, timedelta

# Define the number of SKUs, DCs/FCs, and customers
num_skus = 5
num_dcs = 5
num_customers = 100

# Generate random customer data
customer_zip_codes = [random.randint(10000, 99999) for i in range(num_customers)]
customer_states = [random.choice(
    ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
     'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA',
     'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']) for i in range(num_customers)]
customer_cities = [f'City{i}' for i in range(num_customers)]

# Define shipping methods and warehouses
shipping_methods = ['standard', 'expedited']
warehouses = ['Boston', 'HZ', 'Chicago', 'OTW', 'LA']

# Generate orders with multiple SKUs
orders = []
for i in range(num_customers):
    # Define the number of shipments for the order
    num_shipments = random.choice([1, 2, 3])

    # Generate the order info for each shipment
    for k in range(num_shipments):
        # Define the number of SKUs for the shipment
        num_skus_per_shipment = random.choice([1, 2, 3, 4, 5])

        # Generate the order info for each SKU in the shipment
        for j in range(num_skus_per_shipment):
            # Generate order info
            order_id = f'Order{i}-Shipment{k}-SKU{j}'
            order_date = datetime.now() - timedelta(days=random.randint(1, 365))
            sku_id = f'SKU{j}'
            customer_id = f'Customer{i}'
            customer_zip_code = customer_zip_codes[i]
            customer_state = customer_states[i]
            customer_city = customer_cities[i]
            shipped_warehouse = random.choice(warehouses)
            shipping_method = random.choice(shipping_methods)

            # Append the order info to the list of orders
            orders.append([order_id, order_date, sku_id, customer_id, customer_city,customer_zip_code, customer_state,
                           shipped_warehouse, shipping_method])

# Define the column names for the dataframe
columns = ['order id', 'order date', 'SKU id', 'customer id', 'customer zip code', 'customer state', 'customer city', 'shipped warehouse', 'shipping method']

# Convert the order list to a dataframe
df = pd.DataFrame(orders, columns=columns)

# Display the dataframe
print(df.head())

df.to_csv(r'C:\Users\nimak\OneDrive\Desktop\orders.csv')

