import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Null Hypothesis: Longitude has no predictive value to magnitude of earthquakes

Alternative Hypothesis: Longitude has predictive value to magnitude of earthquakes

I will plot the relationship between longitude and magnitude, while measuring relevant statistical values
'''

# display given data for significance and longitude in scatterplot

loaded_df = pd.read_pickle('earthquake_data.pkl')

data_frame = loaded_df[["magnitude", "longitude"]]

correlation = data_frame["magnitude"].corr(data_frame["longitude"])


plt.scatter(data_frame["magnitude"], data_frame["longitude"])
plt.title(f"FIG 1: Scatter Plot - Correlation: {correlation:.3f}")
plt.xlabel("Magnitude (ML)")
plt.ylabel("Longitude (Degrees)")
plt.show()

# based on the scatterplot shown, we see a couple outliers with high magnitude
# additionally, we can see two general "blocks" of data where one block has a lack of lower magnitude earthquakes (around -50 to 100 degrees)
# one slice on the top seems to better line up with the bottom "block". Since the measure of longitude is CIRCULAR, 
# we can modify the longitude values of the top slice to better represent the data
# through making these modifications, the correlation has fallen, and there are clearly two "blocks" of data revealed

# delete outlier
df_cleaned = data_frame[data_frame["magnitude"] <= 6]

# copy of df for a normal scatterplot
df_scatter = df_cleaned.copy()

# move slice of data to display in a normal scatterplot
df_scatter.loc[df_scatter['longitude'] > 174, 'longitude'] -= 360

correlation = df_scatter["magnitude"].corr(df_scatter["longitude"])

plt.scatter(df_scatter["magnitude"], df_scatter["longitude"])
plt.title(f"Scatter Plot - Correlation: {correlation:.3f}")
plt.xlabel("Magnitude (ML)")
plt.ylabel("Longitude (Degrees)")
plt.show()


# using the same data, do the same but display in a circular scatterplot to better show the circular nature of longitude
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
theta = np.radians(df_cleaned['longitude'])

# Plot scatter points with magnitude as color and size
sc = ax.scatter(theta, df_cleaned['magnitude'], c=df_cleaned['magnitude'], cmap='viridis', s=50, alpha=0.7)

# Set the direction of the angular axis to clockwise
ax.set_theta_direction(-1)

# Set 0 degrees to be at the top of the plot
ax.set_theta_offset(np.pi / 2.0)

ax.set_xlabel('Longitude (degrees)')
ax.set_title('Circular Scatter Plot')
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('magnitude (ML)')
plt.show()


'''
Conclusion:
In the scatterplots of our cleaned data, there is clearly a relationship between longitude and magnitude.

Earthquakes with longitude between ~ negative 45 and ~ positive 175 are seemingly guaranteed to have magnitude over 4 ML,
unlike Earthquakes in other longitudes, which distribute relatively evenly from 0.

There is also a complete lack of earthquakes data from range ~ negative 55 to ~ negative 45.
This is suprising because there is a tectonic plate border close east to that range of longitude
This could indicate a lack of data or something else entirely.

We reject the null hypothesis as knowing longitude has predictive value on the earthquake magnitude, namely the lower bound of magnitude.
'''
