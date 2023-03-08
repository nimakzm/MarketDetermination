import pandas as pd
from geopy.geocoders import Nominatim
import zipcodes

# Load zip code and demand data
df = pd.read_excel(r'C:\Users\nimak\OneDrive\Desktop\BMCs_updated.xlsx')

# Initialize geolocator from Nominatim
geolocator = Nominatim(user_agent="my_app_name")

# Define a function to get latitude and longitude for a zip code
def get_lat_long(zipcode):
    location = geolocator.geocode(zipcode)
    if location:
        return (location.latitude, location.longitude)
    else:
        return (None, None)

# Get a list of all US zip codes
all_zip_codes = [zipcode['zip_code'] for zipcode in zipcodes.list_all()]

# Generate a random sample of 100 zip codes from the list of all zip codes
customer_zipcodes = list(df['Zipcode'])

# Get latitude and longitude for each zip code using the get_lat_long function
latitudes = []
longitudes = []
for zipcode in customer_zipcodes:
    latitude, longitude = get_lat_long(zipcode)
    latitudes.append(latitude)
    longitudes.append(longitude)

df['Latitudes']=latitudes
df['Longitudes']=longitudes

df.to_excel(r'C:\Users\nimak\OneDrive\Desktop\BMCs_latlong.xlsx')


