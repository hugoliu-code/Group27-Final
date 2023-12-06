import earthquakes
import pandas as pd

'''
Column names: 
id
(gap, magnitude, and significance are a part of a larger group called "impact", which may or may not be useful information)
gap
magnitude 
significance
(depth, distance, full, latitude, longitude, and name are part of a larger group called "location")
depth
distance
full (full location name)
latitude
longitude
name
(day, epoch, full, hour, minute, month, second, and year are part of a larger group called "time")
day
epoch
full (combination of year, month, day, hour, minute, second)
hour
minute
month
second
year
'''

# unformatted data from corgi
dictionary_list = earthquakes.get_earthquake()


flattened_dict = dict()

flattened_dict['id'] = [n['id'] for n in dictionary_list]
flattened_dict['gap'] = [n['impact']['gap'] for n in dictionary_list]
flattened_dict['magnitude'] = [n['impact']['magnitude'] for n in dictionary_list]
flattened_dict['significance'] = [n['impact']['significance'] for n in dictionary_list]
flattened_dict['depth'] = [n['location']['depth'] for n in dictionary_list]
flattened_dict['distance'] = [n['location']['distance'] for n in dictionary_list]
flattened_dict['full_location'] = [n['location']['full'] for n in dictionary_list]
flattened_dict['latitude'] = [n['location']['latitude'] for n in dictionary_list]
flattened_dict['longitude'] = [n['location']['longitude'] for n in dictionary_list]
flattened_dict['name'] = [n['location']['name'] for n in dictionary_list]
flattened_dict['day'] = [n['time']['day'] for n in dictionary_list]
flattened_dict['epoch'] = [n['time']['epoch'] for n in dictionary_list]
flattened_dict['full_time'] = [n['time']['full'] for n in dictionary_list]
flattened_dict['hour'] = [n['time']['hour'] for n in dictionary_list]
flattened_dict['minute'] = [n['time']['minute'] for n in dictionary_list]
flattened_dict['month'] = [n['time']['month'] for n in dictionary_list]
flattened_dict['second'] = [n['time']['second'] for n in dictionary_list]
flattened_dict['year'] = [n['time']['year'] for n in dictionary_list]

df = pd.DataFrame(flattened_dict)
df.to_pickle('earthquake_data.pkl')
print(df)

import airlines

# unformatted data from corgi
dictionary_list = airlines.get_airports()

'''

(Under Airport)
Code
Name (full name of airport)

(Under Time)
Label
Month
Month Name
Year


'''

flattened_dict = dict()

flattened_dict['name'] = [n['Airport']['Name'].split(",")[0] for n in dictionary_list]
df = pd.DataFrame(flattened_dict)
df.to_pickle('airline_data.pkl')
print(df)