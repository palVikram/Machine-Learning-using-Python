import pandas as pd

def process_budget_data(file_path, start_year=2017, end_year=2024):
    # Load the data
    matter_budget = pd.read_csv(file_path, encoding="ISO-8859-1", sep="\\t", low_memory=False)
    
    # Filter and sort data by each budget year within the specified range
    budget_data_by_year = {}
    for year in range(start_year, end_year + 1):
        budget_data_by_year[year] = matter_budget[
            matter_budget['Budget Year'] == year
        ][['Matter Number', 'Action Type']].sort_values(by='Budget Year')

    # Create a pivot table with the specified years as columns
    pivot_df = matter_budget.pivot_table(index="Matter Number", columns="Budget Year", values="Budget Amount", fill_value=0)
    
    # Rename columns for better clarity
    pivot_df.columns = [f'budget_{col}' for col in pivot_df.columns]
    
    # Reset index to flatten the table if needed
    pivot_df = pivot_df.reset_index()
    
    return pivot_df

# Example usage
file_path = 'Matter Budget.txt'  # Replace with the actual file path
budget_data = process_budget_data(file_path)
print(budget_data.head())
