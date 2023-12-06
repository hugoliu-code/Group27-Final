import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm

loaded_df = pd.read_pickle('earthquake_data.pkl')

# Assuming 'magnitude' is the column containing earthquake magnitudes
data_frame = loaded_df[["magnitude"]]

# Extract magnitudes as a NumPy array
magnitude_values = data_frame["magnitude"].values

# Perform Anderson-Darling test
result = stats.anderson(magnitude_values)

# Extract test statistic and critical values
statistic = result.statistic
critical_values = result.critical_values

# Print the results
print(f"Anderson-Darling Statistic: {statistic:.2f}")
print(f"Critical Values: {critical_values[2]}")

# Compare the statistic with critical values at a chosen significance level
significance_level = 0.05
reject_null = statistic > critical_values[2]  # Using the critical value at 5% significance level

# Print the result of the test
if reject_null:
    print("Reject the null hypothesis: Magnitudes do not follow a normal distribution.")
else:
    print("Fail to reject the null hypothesis: Magnitudes may follow a normal distribution.")

# Q-Q Plot using statsmodels
qqplot = sm.ProbPlot(magnitude_values, fit=True)
qqplot.qqplot(line='45', alpha=0.5, markerfacecolor='none', markeredgecolor='blue', lw=1)

# Add title
plt.title('Q-Q Plot for Magnitude Data')

# Create a new figure for the histogram and normal distribution fit
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 2)

# Fit a normal distribution to the data
mu, sigma = np.mean(magnitude_values), np.std(magnitude_values)
fit = stats.norm.pdf(np.sort(magnitude_values), mu, sigma)

# Plot histogram of the data
plt.hist(magnitude_values, bins=20, density=True, alpha=0.6, color='g', label='Magnitude Data')

# Plot the normal distribution PDF
plt.plot(np.sort(magnitude_values), fit, '-o', label='Normal Distribution', linewidth=2, color='b')

# Add labels and title
plt.xlabel('Magnitude')
plt.ylabel('Probability Density')
plt.title('Histogram and Normal Distribution Fit for Magnitude Data')
plt.legend()

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()

