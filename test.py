def compute_matter_status(df_matters):
    # Create dictionaries to store statuses for all years
    status_dict = {
        "Opened": {},
        "Resolved": {},
        "Reopen": {},
        "Closed": {}
    }

    # Populate the dictionaries with matter numbers for each year
    for year in df_matters['year'].unique():
        year_str = str(year)
        status_dict["Opened"][year] = df_matters[df_matters['Opened On(Date)'] == year_str]['Matter Number'].tolist()
        status_dict["Resolved"][year] = df_matters[df_matters['Resolved Date'] == year_str]['Matter Number'].tolist()
        status_dict["Reopen"][year] = df_matters[df_matters['Reopened On(Date)'] == year_str]['Matter Number'].tolist()
        status_dict["Closed"][year] = df_matters[df_matters['Date Closed'] == year_str]['Matter Number'].tolist()

    # Define a function to determine the status of a matter based on its year
    def matter_status_check(row):
        year = str(row['year'])
        matter_number = row['Matter Number']

        if matter_number in status_dict["Resolved"].get(year, []):
            return "Resolved"
        elif matter_number in status_dict["Reopen"].get(year, []):
            return "Reopen"
        elif matter_number in status_dict["Opened"].get(year, []):
            return "Open"
        elif matter_number in status_dict["Closed"].get(year, []):
            return "Closed"
        else:
            return "Unknown"

    # Apply the status check function to each row
    df_matters["Matter Status"] = df_matters.apply(matter_status_check, axis=1)

    return df_matters

# Usage
df_matters = compute_matter_status(df_matters)
