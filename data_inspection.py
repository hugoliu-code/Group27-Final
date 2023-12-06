import pandas as pd

# Read the DataFrame from the pickle file
earthquake_df = pd.read_pickle('earthquake_data.pkl')
airline_df = pd.read_pickle('airline_data.pkl')


# Get the number of unique entries in 'name' (City names)
earthquakes_count = set(earthquake_df['name'])
airlines_count = set(airline_df['name'])

print("Number of unique entries in 'Column1':", len(earthquakes_count), len(airlines_count)) # 118 and 26

# how many of these unique entires intersect?
intersection = earthquakes_count.intersection(airlines_count) # 2
print(intersection) # Washington and New York

# In these interesections, how many entires are available in each dataset?
count_earthquakes = (earthquake_df['name'] == 'Washington').sum()
count_airlines = (airline_df['name'] == "Washington").sum()
print(count_earthquakes)

# 171 and 304 for Washington
# 2 and 304 for New York

# Prepare Washington Earthquake data
washington_earthquake_df = earthquake_df[earthquake_df['name'] == 'Washington'].copy()
washington_earthquake_df["month-year"] = washington_earthquake_df["month"].astype(str) + "-" + washington_earthquake_df["year"].astype(str)

unique_times = set(washington_earthquake_df['month-year'])
print(len(unique_times))
print(washington_earthquake_df) # Only have Washington data for 2 months


# Conclusion, both NY and Washington have too little datapoints in one or the other datasets