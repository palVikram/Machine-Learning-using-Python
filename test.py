import pandas as pd

# Function to retrieve a budget field based on Matter Number and column name
def budget_fields(matter_number, column_name, dataframe_budget):
    try:
        value = dataframe_budget[dataframe_budget["Matter Number"] == matter_number][column_name].iloc[0]
        return value
    except IndexError:
        return 0

# Function to retrieve a budget field with additional year filter
def budget_field_s(matter_number, column_name, column_name_2, year, dataframe_budget):
    try:
        value = dataframe_budget[
            (dataframe_budget["Matter Number"] == matter_number) &
            (dataframe_budget[column_name_2] == year)
        ][column_name].iloc[0]
        return value
    except IndexError:
        return "No Budget Given"

# Example usage of these functions:
# Assuming you have a DataFrame called matter_budget and a list of years

# Aggregated budget data grouped by year
matter_budget_agg = matter_budget.groupby(["Budget Year", "Matter Number"], as_index=False)["Budget Amount"].sum()
Matters_list = matter_budget["Matter Number"].tolist()

# Creating last_year_budget and target_year_budget fields for each year
for year in range(2017, 2023):  # Adjust the range as necessary
    matter_budget[f"last_year_budget_{year}"] = matter_budget["Matter Number"].apply(
        lambda x: budget_field_s(x, "Budget Amount", "Budget Year", year - 1, matter_budget)
    )
    matter_budget[f"target_year_budget_{year}"] = matter_budget["Matter Number"].apply(
        lambda x: budget_field_s(x, "Budget Amount", "Budget Year", year, matter_budget)
    )

# Calculating additional fields for each year (e.g., average_budget and ratio_max_average_budget)
for year in range(2017, 2023):
    matter_budget[f"average_budget_{year}"] = matter_budget["Matter Number"].apply(
        lambda x: (budget_field_s(x, "Budget Amount", "Budget Year", year - 1, matter_budget) +
                   budget_field_s(x, "Budget Amount", "Budget Year", year, matter_budget)) / 2
    )
    matter_budget[f"ratio_max_average_budget_{year}"] = matter_budget["Matter Number"].apply(
        lambda x: (
            max(budget_field_s(x, "Budget Amount", "Budget Year", year, matter_budget),
                budget_field_s(x, "Budget Amount", "Budget Year", year - 1, matter_budget))
            /
            ((budget_field_s(x, "Budget Amount", "Budget Year", year, matter_budget) +
              budget_field_s(x, "Budget Amount", "Budget Year", year - 1, matter_budget)) / 2)
        )
    )
