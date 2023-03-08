import random
import pandas as pd
import zipcodes

#
# def getLatLong(customer_zipcodes):
#     latitudes = []
#     longitudes = []
#     for customer in customer_zipcodes:
#         zipcode_info = zipcodes.matching(customer)
#         if zipcode_info:
#             latitudes.append(zipcode_info[0]['lat'])
#             longitudes.append(zipcode_info[0]['long'])
#         else:
#             latitudes.append(None)
#             longitudes.append(None)
#     return latitudes, longitudes
#
# all_zip_codes = [zipcode['zip_code'] for zipcode in zipcodes.list_all()]
# customer_zipcodes = random.sample(all_zip_codes, 100)
#
# latitudes, longitudes = getLatLong(customer_zipcodes)
# forecasted_quantity = [random.randint(1, 1000) for i in range(100)]
#
# dataset = list(zip(customer_zipcodes, forecasted_quantity, latitudes, longitudes))
# columns = ['Zipcode', 'Forecasted Quantity', 'Longitudes', 'Latitudes']
# dataset = pd.DataFrame(dataset, columns=columns)
#
# print(dataset.head())
# dataset.to_csv(r'C:\Users\nimak\OneDrive\Desktop\ZipCodes.csv')

import pandas as pd
import random
import zipcodes

# Load the BMCs file
df = pd.read_excel(r'C:\Users\nimak\OneDrive\Desktop\BMCs.xls')

# Generate random demand values between 1 and 100
demand = [random.randint(1, 100) for i in range(len(df))]
# Add the demand, latitude, and longitude columns to the dataframe
df['demand'] = demand

# Save the modified dataframe to a new file
df.to_excel(r'C:\Users\nimak\OneDrive\Desktop\BMCs_updated.xlsx', index=False)
