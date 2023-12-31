import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Null hypothesis: The significance of an earthquake has a significant difference nor a correlation to the magnitude of earthquakes.
Alternative hypothesis: The significance of an earthquake does not have a correlation and a significance difference to the magnitude of earthquakes.
Goal: Discover relationship between magnitude of an earthquake and its significance
'''

# reading pkl file data & storing info into a dataframe
earthquake_df = pd.read_pickle("earthquake_data.pkl")

# selecting information from earthquakes dataset we are looking for
target_df = earthquake_df[["significance", "magnitude"]]

# determining a correlation between the x/y variables
correlation = target_df["significance"].corr(target_df["magnitude"])

# determining the outlier that is visually noticeable on the plot
# significance = 2674, magnitude = 6.20
# max_val = earthquake_df.sort_values(by="significance", ascending=False)
# print(max_val[["significance", 'magnitude', 'latitude', 'longitude']])

'''
There appears to be a strong correlation between these two variables. 
There is an outlier at (significance = 2674, magnitude = 6.20). This is located in Norcia, Italy. 
'''

# creating scatter plot (axes, title, dataset information)
plt.scatter(target_df["magnitude"], target_df["significance"])
plt.title(f"Magnitude and Significance (Correlation Coefficient: {correlation:.2f})")
plt.xlabel("Magnitude (Richter Scale)")
plt.ylabel("Significance")

'''
The line of best fit will show how well the variables relate by showing how well they snug around this said line. 
For further investigations of the accuracy/reliability of the data, an r^2 value will be calculated. 
The r^2 value will show how well the line of best fit matches the dataset thus validating the data.
'''

# creating line of best fit
x = np.array(target_df["magnitude"])
y = np.array(target_df["significance"])
m, b = np.polyfit(x, y, 1)
linear_eq = m*x + b

# adding line of best fit to the plot ( y = mx + b)
plt.scatter(x, y)
plt.plot(x, linear_eq)

# finding r^2 correlation to determine the goodness of the model
sum_residuals = np.sum((y - linear_eq) ** 2)
sum_squares = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - (sum_residuals / sum_squares)
print(f"R-squared value: {r_squared:.4f}")

# scatter plot with information on correlation coefficient & relationship between magnitude & significance
plt.show()

'''
The data shows that there is a strong positive correlation between the magnitude of an earthquake and its corresponding significance. 
The null hypothesis is thus accepted and the alternative hypothesis is rejected. 
From the dataset though, it is curious to see which areas of the world from 2000-2016 have the highest percentage of most impactful earthquakes (greater than 5.5 on Richter Scale)
& if those earthquakes are located near tectonic plates.
'''
