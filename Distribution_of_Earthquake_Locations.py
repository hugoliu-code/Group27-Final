from geopy.geocoders import Nominatim
import pandas as pd
import matplotlib.pyplot as plt

'''
The goal of this pie chart is to further explore some of the relationships discovered from the prior scatter plot. 
Most specifically, this pie chart will display the distribution of earthquakes with a magnitude greater than or equal to 5.5.

Null Hypothesis: Most earthquakes are distributed close to areas with tectonic plates. 
Alternative Hypothesis: Most earthquakes are not distributed close to areas with tectonic plates. 
'''

# earthquake data points that are above 4.5 (considered most impactful)
loaded_df = pd.read_pickle('earthquake_data.pkl')
filtered_df = loaded_df[loaded_df['magnitude'] > 5.5]

'''
The original plan was to use the Geopy module.geopy to get the country that pertains to a certain latitude and longitude.
However, it was discovered that the coordinates provided from the dataset are incompatible with the data of coordinates in the module.
For this reason, the module identified that the majority of earthquakes were located in the United States. 
According to the pie chart and map correctly displaying the information regarding earthquake location, this is incorrect.
As a result, it was decided that the latitudes/longitudes would be manually identified with an online coordianate to address converter.
The results are given in a dictionary called list_count.
'''

list_count = {
    'Indonesia': 4,
    'Argentina': 1,
    'Philippine Sea': 3,
    'Indian Ocean': 3,
    'United States': 1,
    'South Atlantic Ocean': 3,
    'United Kingdom': 1,
    'North Pacific Ocean': 3,
    'Soloman Islands': 1,
    'South Pacific Ocean': 3,
    'Russia': 1,
    'Australia': 1,
    'Italy': 1,
    'Myanmar': 1,
    'Jordan': 1
}


'''
The commented code below demonstrates the line of thinking that would have been utilized if the 
converter module had coordinates that were compatible with the ones found in the dataset.
'''

# lat = loaded_df["latitude"].tolist()
# long = loaded_df["longitude"].tolist()
# geolocator = Nominatim(user_agent="http")
# countries = []
# count = 1

# for i in range(0, len(filtered_df)):
#     coordinate = f"{lat[i]}, {long[i]}"
#     location = geolocator.reverse(coordinate)
#     # print(location)
#     if location is not None:
#         country_name = location.raw.get('address', {}).get('country')
#         if country_name:
#             countries.append(country_name)
#             print(country_name)
#     else:
#         print(f"{count}. No location found for coordinates: {coordinate}")
#         count += 1
#
# for i, value in enumerate(countries):
#     if value == "မြန်မာ":
#         countries[i] = "Myanmar"
#
# country_count = {}
# for country in countries:
#     if country in country_count:
#         country_count[country] += 1
#     else:
# #         country_count[country] = 1
#
# print(country_count)

# creating the pie chart
labels = list(list_count.keys())
sizes = list(list_count.values())

plt.figure(figsize=(8,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0)
plt.axis('equal')
plt.title('Distribution of Locations of Earthquakes with Magnitude >= 5.5')

# Show the plot
plt.show()

'''
The pie chart distributions show that the majority of major earthquakes occur 
in the North Pacific Ocean, Philippine Sea, Indian Ocean, South Pacific Ocean, South Atlantic Ocean, and Indonesia.
See new_map.py for further analysis
'''
