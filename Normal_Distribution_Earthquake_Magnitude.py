import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

loaded_df = pd.read_pickle('earthquake_data.pkl')

data_frame = loaded_df[["magnitude"]]

# Extract magnitudes as a NumPy array
magnitude_values = data_frame["magnitude"].values

# Perform anderson-darling test
result = stats.anderson(magnitude_values)
statistic = result.statistic
critical_values = result.critical_values
print(f"Anderson-Darling Statistic: {statistic:.2f}")
print(f"Critical Values: {critical_values[2]}")

# Compare the statistic with critical values
significance_level = 0.05
reject_null = statistic > critical_values[2]
if reject_null:
    print("Reject the null hypothesis: Magnitudes do not follow a normal distribution.")
else:
    print("Fail to reject the null hypothesis: Magnitudes may follow a normal distribution.")

# Q-Q Plot using statsmodels
stats.probplot(magnitude_values, plot=plt)
plt.title('Q-Q Plot for Magnitude Data')

# Create a new figure for the histogram
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 2)
mu, sigma = np.mean(magnitude_values), np.std(magnitude_values)
fit = stats.norm.pdf(np.sort(magnitude_values), mu, sigma)
plt.hist(magnitude_values, bins=20, density=True, alpha=0.6, color='g', label='Magnitude Data')
plt.plot(np.sort(magnitude_values), fit, '-o', label='Normal Distribution', linewidth=2, color='b')
plt.xlabel('Magnitude')
plt.ylabel('Probability Density')
plt.title('Histogram and Normal Distribution Fit for Magnitude Data')
plt.legend()
plt.tight_layout()
plt.show()

