"""
Step 1: Column selection.

Keeps only the columns relevant to this project out of the raw survey's 172:
- MainBranch: needed later to filter down to professional developers
- The 6 student-providable feature columns
- DevType: the label

Everything else (compensation, job satisfaction, AI tool opinions, workplace
tools, Stack Overflow community usage, etc.) is dropped -- not relevant to
predicting career path from a student's skills and education.
"""

import pandas as pd

df = pd.read_csv('/home/chris/Documents/College/Roadmap-Project/repo/train_model/results.csv', low_memory=False)
print(f"Starting columns: {len(df.columns)}")

keep_cols = [
    'MainBranch',
    'EdLevel',
    'YearsCode',
    'LanguageHaveWorkedWith',
    'DatabaseHaveWorkedWith',
    'PlatformHaveWorkedWith',
    'WebframeHaveWorkedWith',
    'DevType',
]

df = df[keep_cols]
print(f"Columns kept: {len(df.columns)}")
print(f"Rows: {len(df)}")

df.to_csv('/home/chris/Documents/College/Roadmap-Project/repo/train_model/clipped_data.csv', index=False)
print("\nSaved to clipped_data.csv")