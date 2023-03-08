import pandas as pd
import random
import zipcodes

def getLatLong(customer_zipcodes):
    # Define two empty lists to store latitude and longitude values
    latitudes = []
    longitudes = []

    # Loop through all customer zip codes
    for customer in customer_zipcodes:
        # Use zipcodes library to get the latitude and longitude values of each zip code
        location = zipcodes.matching(customer)[0]
        latitudes.append(location['lat'])
        longitudes.append(location['long'])

    return latitudes, longitudes

# Get a list of all US zip codes
all_zip_codes = [zipcode['zip_code'] for zipcode in zipcodes.list_all()]

# Generate a random sample of 100 zip codes from the list of all zip codes
customer_zipcodes = random.sample(all_zip_codes, 10000)

latitudes, longitudes = getLatLong(customer_zipcodes)

# Generate random forecasted quantity for each customer
forecasted_quantity = [random.randint(1, 30) for i in range(10000)]

# Combine zipcodes and forecasted quantity into a list of tuples
dataset = list(zip(customer_zipcodes, forecasted_quantity, latitudes, longitudes))

# Define the column names for the dataframe
columns = ['Zipcode', 'Forecasted Quantity', 'Latitudes', 'Longitudes']

# Convert the order list to a dataframe
dataset = pd.DataFrame(dataset, columns=columns)

print(dataset)

dataset.to_csv(r'C:\Users\nimak\OneDrive\Desktop\orders.csv')
