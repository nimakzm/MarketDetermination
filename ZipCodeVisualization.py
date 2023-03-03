import pandas as pd
import folium
from folium.plugins import MarkerCluster
import webbrowser
import zipcodes


ds=pd.read_csv(r'C:\Users\nimak\OneDrive\Desktop\ZipCOdes.csv', dtype={'Zipcode': str})

df=pd.read_excel(r'C:\Users\nimak\OneDrive\Desktop\BMCs.xls', dtype={'Zipcode': str})

#
# # Filter out invalid zip codes
# valid_zips = []
# for index, row in df.iterrows():
#     if zipcodes.matching(row['Zipcode']):
#         valid_zips.append(index)
# df = df.iloc[valid_zips]
# # Save the filtered dataframe back to CSV
# df.to_csv('ZipCOdes.csv', index=False)
# df=pd.read_csv(r'C:\Users\nimak\OneDrive\Desktop\ZipCOdes.csv')


# create a map centered at the US
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4, crs='EPSG3857')

# create a marker cluster for the zip code markers
marker_cluster = MarkerCluster().add_to(m)

# add a marker for each zip code with its coordinates
for i, row in df.iterrows():
    zipcode_info = zipcodes.matching(row['Zipcode'])
    if zipcode_info:
        folium.Marker(location=[zipcode_info[0]['lat'], zipcode_info[0]['long']],
                      popup=row['Zipcode']).add_to(marker_cluster)

output_file = "map2.html"
m.save(output_file)
webbrowser.open(output_file, new=2)  # open in new tab

