def target_year_invoice(df, year, matter_number):
    # Filter DataFrame directly based on the specified year and matter number
    target_row = df[(df['Year'] == year + 1) & (df['Matter Number'] == matter_number)]
    
    # Return the invoice cost if the row exists, else return None
    if not target_row.empty:
        return target_row['invoice_cost'].iloc[0]
    else:
        return None
