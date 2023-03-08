import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2
import pgeocode

# Load zip code and demand data
df = pd.read_excel(r'C:\Users\nimak\OneDrive\Desktop\BMCs_updated.xlsx')

# Define warehouse locations
warehouses = ['Boston', 'Hazelton', 'Chicago', 'Ottawa', 'Dallas', 'Fontana']
warehouses_zipcode = [1434, 18202, 60642, 66067, 75220, 92335]
warehouses_capacity = [100000, 80000, 120000, 70000, 90000, 100000] # assumed capacity of each warehouse

# Define a function to calculate the distance betweek two zipcodes
def distance(zip1, zip2):
    nomi = pgeocode.Nominatim('US')
    loc1 = nomi.query_postal_code(str(zip1))
    loc2 = nomi.query_postal_code(str(zip2))
    lat1, lon1 = radians(loc1.latitude), radians(loc1.longitude)
    lat2, lon2 = radians(loc2.latitude), radians(loc2.longitude)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    r = 3958.8  # radius of Earth in miles
    return r * c


# Initialize the assigned warehouse for each zip code to None
df['assigned_warehouse'] = np.nan

# Iterate over each zip code
for i, row in df.iterrows():
    # Calculate the distance between the zip code and each warehouse
    distances = [distance(row['Zipcode'], warehouse) for warehouse in warehouses_zipcode]
    # Sort the distances in ascending order
    sorted_distances = sorted(zip(distances, warehouses, warehouses_capacity), key=lambda x: x[0])
    # Iterate over the sorted warehouses until a warehouse with enough capacity is found
    for d, w, c in sorted_distances:
        if row['Demand'] <= c:
            # Assign the zip code to the warehouse and subtract the demand from its capacity
            df.at[i, 'assigned_warehouse'] = w
            idx = warehouses.index(w)
            warehouses_capacity[idx] -= row['Demand']
            break

# Print the number of zip codes assigned to each warehouse
print(df.groupby('assigned_warehouse')['Zipcode'].count())

df.to_excel(r'C:\Users\nimak\OneDrive\Desktop\BMCs_Warehouses.xlsx')

# Set a threshold of the demand that should be met

# We need to check the transportation lane to make sure the warehouse can serve the zip code