import pandas as pd
import folium
from folium.plugins import MarkerCluster
import webbrowser
import zipcodes

df = pd.read_excel(r'C:\Users\nimak\OneDrive\Desktop\BMCs_updated.xlsx', dtype={'Zipcode': str})


# Create a map centered at the US
map = folium.Map(location=[37.0902, -95.7129], zoom_start=4, crs='EPSG3857')

# Create a marker cluster for the zip code markers
marker_cluster = MarkerCluster().add_to(map)

# Add a marker for each zip code with its coordinates and demand
for i, row in df.iterrows():
    zipcode_info = zipcodes.matching(row['Zipcode'])
    if zipcode_info:
        popup_text = f"Zipcode: {row['Zipcode']}<br>Demand: {row['Demand']}"
        folium.Marker(location=[zipcode_info[0]['lat'], zipcode_info[0]['long']],
                      popup=popup_text).add_to(marker_cluster)

# Add markers for warehouse locations
warehouses = ['Boston', 'Hazelton', 'Chicago', 'Ottawa', 'Dallas', 'Fontana']
warehouses_zipcodes = [1434, 18202, 60642, 66067, 75220, 92335]
for i in range(len(warehouses)):
    warehouse_info = zipcodes.matching(str(warehouses_zipcodes[i]))
    if warehouse_info:
        popup_text = f"Warehouse: {warehouses[i]}"
        folium.Marker(location=[warehouse_info[0]['lat'], warehouse_info[0]['long']],
                      popup=popup_text, icon=folium.Icon(color='red')).add_to(marker_cluster)

output_file = "map2.html"
print(output_file)
map.save(output_file)
webbrowser.open(output_file, new=2)  # open in new tab
