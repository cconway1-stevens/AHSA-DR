import numpy as np
import pandas as pd
from scipy.stats import ttest_rel
from statistics import mode

# Load data from CSV
data = pd.read_csv('data - Sheet1.csv')

# Extract the necessary columns
pre_data = data['Pre-Survey: November 2023']
post_data = data['Post-Survey: March 2024']

# Calculate statistics for Pre-Survey
pre_mean = np.mean(pre_data)
pre_median = np.median(pre_data)
pre_mode = mode(pre_data)
pre_range = np.max(pre_data) - np.min(pre_data)
pre_lowest = np.min(pre_data)
pre_highest = np.max(pre_data)
pre_sd = np.std(pre_data)

# Calculate statistics for Post-Survey
post_mean = np.mean(post_data)
post_median = np.median(post_data)
post_mode = mode(post_data)
post_range = np.max(post_data) - np.min(post_data)
post_lowest = np.min(post_data)
post_highest = np.max(post_data)
post_sd = np.std(post_data)

# Perform t-test
t_stat, p_value = ttest_rel(pre_data, post_data)

# Prepare results
pre_stats = {
    "Mean": pre_mean,
    "Median": pre_median,
    "Mode": pre_mode,
    "Range": pre_range,
    "Lowest": pre_lowest,
    "Highest": pre_highest,
    "Standard Deviation": pre_sd
}

post_stats = {
    "Mean": post_mean,
    "Median": post_median,
    "Mode": post_mode,
    "Range": post_range,
    "Lowest": post_lowest,
    "Highest": post_highest,
    "Standard Deviation": post_sd
}

t_test_results = {
    "T-Statistic": t_stat,
    "P-Value": p_value,
    "Significant": p_value < 0.05  # Typically, a p-value less than 0.05 indicates statistical significance
}

print(pre_stats,"\n\n", post_stats,"\n\n", t_test_results)
