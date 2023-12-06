import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# take the dictionary of data from the corgi website and convert it to a pickle file
loaded_df = pd.read_pickle('earthquake_data.pkl')

# convert the data into a Pandas dataframe with the magnitude and depth
data_frame = loaded_df[["magnitude", "depth"]]

# finds the correlation between the magnitude and depth data using the correlation function
correlation = data_frame["magnitude"].corr(data_frame["depth"])
sample_size = len(loaded_df)

# sets the threshold and alpha for the test statistic calculation which is used to find the p-value
threshold = 0.75
alpha = 0.01
t_statistic = (correlation - threshold) / np.sqrt((1 - correlation**2) / (sample_size - 2))

# calculation to find the p-value
p_value = (1 - stats.t.cdf(abs(t_statistic), sample_size - 2))

# sets the title, x-axis and y-axis, and prints the magnitude and depth data
plt.scatter(data_frame["magnitude"], data_frame["depth"])
plt.title(f"Scatter Plot - Correlation: {correlation:.3f}, p-value: {p_value:.4f}\n(Each dot is an individual earthquake)")
plt.xlabel("Magnitude (Richter Scale)")
plt.ylabel("Depth (km)")
plt.show()

# prints the original hypothesis and result for the user
print(f"Null Hypothesis: r <= {alpha}")
print(f"Alternate Hypothesis:  r < {alpha}")
print(f"Correlation: {correlation}")
print(f"P-Value: {p_value}\n")

if p_value < alpha:
    print(f"Because the p-value is less than {alpha} we reject the hypothesis that r is greater than or equal to 0.75.")
    print("There is a relatively weak correlation between earthquake magnitude and depth")
else:
    print(f"Because the p-value is greater than {alpha} we fail to reject the hypothesis that r is greater than or equal to 0.75.")
    print("There is a strong correlation between earthquake magnitude and depth")

"""
Conclusion:
In the scatterplots of our cleaned data, there is little to no relationship between magnitude and depth. 

Earthquakes are relatively evenly distributed between the magnitude of 0-6 and depths of 0-300 km.

There are some outliers of earthquakes around 4-5 magnitude which may be because only few places can sense earthquakes at those depths. 
This is surprising because originally I believed there would be a strong postive correlation between depth and strength.
I believed this because deep earthquakes would have more energy from the earth's core. 

Because the p-value is less than 0.01 we reject the null hypothesis that r is greater than or equal to 0.75.
"""
