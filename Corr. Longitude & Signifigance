import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Null Hypothesis: Longitude has no predictive value to significance of earthquakes

Alternative Hypothesis: Longitude has predictive value to significance of earthquakes

I will plot the relationship between longitude and significance, while measuring relevant statistical values
'''

# display given data for significance and longitude in scatterplot

loaded_df = pd.read_pickle('earthquake_data.pkl')

data_frame = loaded_df[["significance", "longitude"]]

correlation = data_frame["significance"].corr(data_frame["longitude"])


plt.scatter(data_frame["significance"], data_frame["longitude"])
plt.title(f"Scatter Plot - Correlation: {correlation:.3f}")
plt.xlabel("Significance (Mw)")
plt.ylabel("Longitude (Degrees)")
plt.show()

# based on the scatterplot shown, we see an outlier in significance around (2500 Mw, 0 degrees)
# additionally, we can see two general "blocks" of data where one block has a lack of lower significance earthquakes (around -50 to 100 degrees)
# one slice on the top seems to better line up with the bottom "block". Since the measure of longitude is CIRCULAR, 
# we can modify the longitude values of the top slice to better represent the data
# through making these modifications, the correlation has jumped from 0.646 to 0.679, and there are clearly two "blocks" of data revealed

# delete outlier
df_cleaned = data_frame[data_frame["significance"] <= 2500]

# copy of df for a normal scatterplot
df_scatter = df_cleaned.copy()

# move slice of data to display in a normal scatterplot
df_scatter.loc[df_scatter['longitude'] > 174, 'longitude'] -= 360

correlation = df_scatter["significance"].corr(df_scatter["longitude"])

plt.scatter(df_scatter["significance"], df_scatter["longitude"])
plt.title(f"Scatter Plot - Correlation: {correlation:.3f}")
plt.xlabel("Significance (Mw)")
plt.ylabel("Longitude (Degrees)")
plt.show()


# using the same data, do the same but display in a circular scatterplot to better show the circular nature of longitude
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
theta = np.radians(df_cleaned['longitude'])

# Plot scatter points with significance as color and size
sc = ax.scatter(theta, df_cleaned['significance'], c=df_cleaned['significance'], cmap='viridis', s=50, alpha=0.7)

# Set the direction of the angular axis to clockwise
ax.set_theta_direction(-1)

# Set 0 degrees to be at the top of the plot
ax.set_theta_offset(np.pi / 2.0)

ax.set_xlabel('Longitude (degrees)')
ax.set_title('Circular Scatter Plot')
cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Significance (Mw)')
plt.show()


'''
Conclusion:
In the scatterplots of our cleaned data, there is clearly a relationship between longitude and significance.

Earthquakes with longitude between ~ negative 45 and ~ positive 175 are seemingly guaranteed to have significance over 200 Mw,
unlike Earthquakes in other longitudes, which distribute relatively evenly from 0.

There is also a complete lack of earthquakes data from range ~ negative 55 to ~ negative 45.
This is suprising because there is a tectonic plate border close east to that range of longitude
This could indicate a lack of data or something else entirely.

We reject the null hypothesis as knowing longitude has predictive value on the earthquake significance, namely the lower bound of significance.
'''
