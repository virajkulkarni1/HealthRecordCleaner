import pandas as pd
import matplotlib.pyplot as plt
import os

RAW_PATH = os.path.join('data', 'raw_patients.csv')
CLEANED_PATH = os.path.join('data', 'cleaned_patients.csv')

# Load data
df_raw = pd.read_csv(RAW_PATH)
df_clean = pd.read_csv(CLEANED_PATH)

# Count conditions
raw_counts = df_raw['condition'].fillna('Missing').value_counts().sort_index()
clean_counts = df_clean['condition'].fillna('Missing').value_counts().sort_index()

# Plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
raw_counts.plot(kind='bar', ax=axes[0], color='skyblue', title='Raw Condition Counts')
clean_counts.plot(kind='bar', ax=axes[1], color='seagreen', title='Cleaned Condition Counts')
axes[0].set_ylabel('Count')
axes[0].set_xlabel('Condition')
axes[1].set_xlabel('Condition')
plt.tight_layout()
plt.savefig('data/condition_comparison.png')
plt.show()
print('Saved plot to data/condition_comparison.png')

