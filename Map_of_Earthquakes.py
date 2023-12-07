import folium
import pandas as pd

'''
This map relates to the information given by the pie chart on the distribution of locations of earthquakes with a magnitude >= 5.5.
It will show where in the world the earthquakes with the largest magnitude occur.
'''

# earthquake data points that are above 5.5 (considered most impactful)
loaded_df = pd.read_pickle('earthquake_data.pkl')
filtered_df = loaded_df[loaded_df['magnitude'] > 5.5]

# take the filtered data's info and take the info of lat + long indv
lat = filtered_df["latitude"].tolist()
long = filtered_df["longitude"].tolist()

# creating the interactive map
l_map = folium.Map(location=[30,-100], zoom_start=2)

coordinate_point = []

for i in range(0, len(filtered_df)):
    coordinate_point.append({"location": [lat[i], long[i]]})

for point in coordinate_point:
    folium.Marker(location=point["location"]).add_to(l_map)

# Save the map to an HTML file
l_map.save("map.html")

'''
Comparing this map of information to a map displaying the locations of tectonic plates, 
it is clear that the majority of the most impactful earthquakes occur within this region.
Therefore, the null hypothesis is accepted that earthquakes are distributed close to areas with tectonic plates. 
'''
