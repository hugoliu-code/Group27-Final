import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


loaded_df = pd.read_pickle('earthquake_data.pkl')

data_frame = loaded_df[["magnitude", "depth"]]

correlation = data_frame["magnitude"].corr(data_frame["depth"])
sample_size = len(loaded_df)

threshold = 0.75
alpha = 0.01
t_statistic = (correlation - threshold) / np.sqrt((1 - correlation**2) / (sample_size - 2))

p_value = (1 - stats.t.cdf(abs(t_statistic), sample_size - 2))

plt.scatter(data_frame["magnitude"], data_frame["depth"])
plt.title(f"Scatter Plot - Correlation: {correlation:.3f}, p-value: {p_value:.4f}\n(Each dot is an individual earthquake)")
plt.xlabel("Magnitude (Richter Scale)")
plt.ylabel("Depth (km)")
plt.show()


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

