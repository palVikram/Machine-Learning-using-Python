import pandas as pd

def calculate_budget_statistics(pivot_df, years):
    # Calculate max budget for each year and add it to new columns
    for year in years:
        pivot_df[f"max_budget_{year}"] = pivot_df[f"budget_{year}"].max(axis=1).round(2)

    # Calculate average budget for each year and add it to new columns
    for i, year in enumerate(years):
        if i == 0:
            pivot_df[f"average_budget_{year}"] = pivot_df[f"budget_{year}"].tolist()
        else:
            avg_column = pivot_df[[f"budget_{years[j]}" for j in range(i+1)]].mean(axis=1).tolist()
            pivot_df[f"average_budget_{year}"] = avg_column

    # Calculate the ratio of max budget to average budget for each year and add to new columns
    for year in years:
        pivot_df[f"ratio_max_average_budget_{year}"] = (
            pivot_df[f"max_budget_{year}"] / pivot_df[f"average_budget_{year}"]
        ).round(2)
    
    return pivot_df

# Example usage
# Assuming 'pivot_df' is the DataFrame created from the previous function
years = [2017, 2018, 2019, 2020, 2021, 2022]  # Replace with the specific years you have
pivot_df = calculate_budget_statistics(pivot_df, years)

# Display the first few rows
print(pivot_df.head())
