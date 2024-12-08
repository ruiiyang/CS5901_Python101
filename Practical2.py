import pandas as pd
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('../P2data5117.csv', delimiter='\t')  # Use '\t' tab-separated

# Remove extra spaces in string-type columns
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

# Display the cleaned DataFrame
# print(df)

# print (df.describe() )


def not_describe(df):
    """
    Manually computes summary statistics similar to df.describe()
    for all numeric columns in the given DataFrame.
    """
    # Initialize an empty dictionary to store summary statistics for each column
    summary_stats = {}

    # Iterate over each numeric column in the DataFrame
    for col in df.select_dtypes(include=[np.number]).columns:
        data = df[col].dropna()  # Exclude NaN values for calculations
        
        # Calculate each statistic manually
        count = len(data)
        mean = data.mean()
        std_dev = data.std()
        min_val = data.min()
        q1 = data.quantile(0.25)
        median = data.median()
        q3 = data.quantile(0.75)
        max_val = data.max()
        
        # Store the statistics in a dictionary for the column
        summary_stats[col] = {
            'count': count,
            'mean': mean,
            'std': std_dev,
            'min': min_val,
            '25%': q1,
            '50%': median,
            '75%': q3,
            'max': max_val
        }

    # Convert the dictionary to a DataFrame for a table-like view
    summary_df = pd.DataFrame(summary_stats) 

    return summary_df


# Call the function
# print(not_describe(df))

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df)