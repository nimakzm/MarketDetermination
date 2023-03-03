import random
import pandas as pd
import zipcodes


def getLatLong(customer_zipcodes):
    latitudes = []
    longitudes = []
    for customer in customer_zipcodes:
        zipcode_info = zipcodes.matching(customer)
        if zipcode_info:
            latitudes.append(zipcode_info[0]['lat'])
            longitudes.append(zipcode_info[0]['long'])
        else:
            latitudes.append(None)
            longitudes.append(None)
    return latitudes, longitudes

all_zip_codes = [zipcode['zip_code'] for zipcode in zipcodes.list_all()]
customer_zipcodes = random.sample(all_zip_codes, 100)

latitudes, longitudes = getLatLong(customer_zipcodes)
forecasted_quantity = [random.randint(1, 1000) for i in range(100)]

dataset = list(zip(customer_zipcodes, forecasted_quantity, latitudes, longitudes))
columns = ['Zipcode', 'Forecasted Quantity', 'Longitudes', 'Latitudes']
dataset = pd.DataFrame(dataset, columns=columns)

print(dataset.head())
dataset.to_csv(r'C:\Users\nimak\OneDrive\Desktop\ZipCodes.csv')
