## creating function for introducing other column based on a condition
def introduce_other(df , column_name, threshold):
    # Count the occurrences of each category in the column
    counts = df[column_name].value_counts()
    
    # Identify categories with occurrences below the threshold
    categories_to_replace = counts[counts < threshold].index
    
    # Replace those categories with "Other"
    df[column_name] = df[column_name].replace(categories_to_replace, 'Other')
    
    # Return the updated value counts
    return df[column_name].value_counts()

## creating a function that will find those column name where Any specific column name is presenet
def find_columns(df, column):
    all_cols = [col for col in df.columns for target_col in column if target_col in col]
    return all_cols
