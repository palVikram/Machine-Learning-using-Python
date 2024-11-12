import pandas as pd

# Assuming `matter_df`, `invoice_df`, and `budget_df` are your DataFrames for matter, invoice, and budget data

# Define the years you are working with
years = [2017, 2018, 2019, 2020, 2021, 2022]  # Adjust based on available data

# Initialize an empty list to store yearly merged data
merged_data_by_year = []

# Loop through each year to process data for each year individually
for year in years:
    # Extract invoice and budget columns for the specific year
    invoice_columns = ["Matter Number", f"invoice_cost_{year}", f"max_invoice_cost_{year}"]
    budget_columns = ["Matter Number", f"budget_{year}", f"max_budget_{year}"]

    # Select relevant data for the current year from invoice and budget
    invoice_data = invoice_df[invoice_columns]
    budget_data = budget_df[budget_columns]
    
    # Merge matter data with invoice and budget data for the current year
    merged_year_data = matter_df.merge(invoice_data, on="Matter Number", how="left").merge(budget_data, on="Matter Number", how="left")
    
    # Add a column to indicate the year for this combined data
    merged_year_data["Year"] = year
    
    # Append the merged data for this year to the list
    merged_data_by_year.append(merged_year_data)

# Concatenate all yearly data into a single DataFrame
final_combined_df = pd.concat(merged_data_by_year, ignore_index=True)

# Display the resulting combined DataFrame
print(final_combined_df.head())
