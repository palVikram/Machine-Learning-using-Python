def get_target_year_invoice(row, df):
    # Filter the DataFrame for the next year and the specific matter number
    target_row = df[(df['Year'] == row['Year'] + 1) & (df['Matter Number'] == row['Matter Number'])]
    
    # Return the invoice cost if the row exists, else return None
    if not target_row.empty:
        return target_row['invoice_cost'].iloc[0]
    else:
        return None

# Apply the function to each row of the DataFrame
df['next_year_invoice'] = df.apply(lambda row: get_target_year_invoice(row, df), axis=1)
