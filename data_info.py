import pandas as pd
def inspect_data(df):
    print("\n***GENERAL INFO ABOUT %s***" %df.name)
    print("\n")
    print(df.columns)
    print("\n")
    print(df.info())
    print("\nDistribution of values:")
    print(df.describe())
    print("\nFirst 3 rows:")
    print(df.head(3))
    print("\nNA per column:")
    print(df.isna().sum())