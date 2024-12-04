import pandas as pd
import numpy as np
import logging
import warnings
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Ignore warnings for cleaner logs
warnings.filterwarnings("ignore")

# Configure logging
logging.basicConfig(
    filename="invoice_cost_prediction.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Import custom utility functions
from process_invoice import (
    process_data,
    calculate_statistics,
    check_action_type,
    budget_calculation,
    invoice_calculation,
    budget_end_date,
    budget_length,
    check_lifetime_invoice_cost,
    check_lifetime_budget,
    read_pickle_file,
    merge_matter_invoice_budget,
    conversion_rate
)

# Load pickled resources
def load_pickle_file(filepath):
    try:
        logging.info(f"Loading pickled file from {filepath}.")
        with open(filepath, "rb") as file:
            return pickle.load(file)
    except Exception as e:
        logging.error(f"Error loading pickled file from {filepath}: {str(e)}")
        raise

# File paths
scaler_filepath = '/mnt/data/legal/matter_data/invoice_cost_prediction/scaler.pkl'
categorical_columns_map_filepath = '/mnt/data/legal/matter_data/invoice_cost_prediction/categorical_columns_map.pkl'
scaler_target_filepath = '/mnt/data/legal/matter_data/invoice_cost_prediction/scaler_target.pkl'
model_filepath = '/mnt/data/legal/matter_data/invoice_cost_prediction/model.pkl'

# Load resources
scaler = load_pickle_file(scaler_filepath)
categorical_columns_map = load_pickle_file(categorical_columns_map_filepath)
scaler_target = load_pickle_file(scaler_target_filepath)
model = load_pickle_file(model_filepath)

# Define date range for processing
data_start_date = 2022
data_end_date = 2023

# Chunk size for large file processing
chunk_size = 100000

# Main pipeline
def main():
    try:
        logging.info("Starting the invoice cost prediction pipeline.")

        # Filepaths for datasets
        matters_filepath = "/mnt/data/legal/matter_data/Matters.txt"
        budget_filepath = "/mnt/data/legal/matter_data/Matter Budget.txt"
        invoice_filepath = "/mnt/data/legal/invoice_data/Invoiceheaders_remove_lineend.txt"

        # Load datasets
        matters = pd.DataFrame()
        for chunk in pd.read_csv(matters_filepath, chunksize=chunk_size, sep='^', encoding='ISO-8859-1', low_memory=False):
            matters = pd.concat([matters, chunk], ignore_index=True)

        matter_budget = pd.read_csv(budget_filepath, sep='^', encoding='ISO-8859-1', low_memory=False)
        invoice_header = pd.read_csv(invoice_filepath, sep='^', encoding='ISO-8859-1', low_memory=False)

        logging.info("Datasets loaded successfully.")

        # Preprocess data
        matters = process_data(matters)
        matter_budget = process_data(matter_budget)
        invoice_header = process_data(invoice_header)

        # Add derived columns
        matters["Action_Type"] = matters["Matter Number"].apply(lambda x: check_action_type(matter_budget, x))

        # Merge datasets
        final_combined_df = merge_matter_invoice_budget(data_start_date, invoice_header, matter_budget, matters)

        # Add budget and invoice calculations
        final_combined_df["Target_year_budget"] = final_combined_df.apply(lambda x: budget_calculation(x, matter_budget), axis=1)
        final_combined_df["Invoice_Calculated"] = final_combined_df.apply(lambda x: invoice_calculation(x, invoice_header), axis=1)

        # Add additional metrics
        final_combined_df["budget_length"] = final_combined_df.apply(budget_length, axis=1)
        final_combined_df["Lifetime_Invoice_Validated"] = final_combined_df.apply(lambda x: check_lifetime_invoice_cost(x), axis=1)
        final_combined_df["Lifetime_Budget_Validated"] = final_combined_df.apply(lambda x: check_lifetime_budget(x), axis=1)

        # Apply conversion rates
        final_combined_df["Invoice_Total_Converted"] = final_combined_df["Invoice Total"].apply(lambda x: conversion_rate(x))

        # Prepare test data
        test = final_combined_df[final_combined_df["type"] == "test"]
        X_test = test.drop("Target_year", axis=1)
        y_test = test["Target_year"]

        # Encode categorical columns
        categorical_columns = [
            'Subject Area', 'Matter Type', 'J&J Role', 'Cost Center Sector',
            'Action Type', 'Matter_Country_State', 'J&J Reporting Client Sector', 'Matter Status'
        ]
        X_test = encode_categorical_columns(X_test, "Target_year", categorical_columns)

        # Scale numerical data
        numerical_columns = [
            'lifetime_budget', 'lifetime_invoice_cost', 'max_budget', 'average_budget',
            'ratio_max_average_invoice_cost', 'last_year_budget', 'last_year_invoice_cost',
            'Subject Area_Encoded', 'Matter Type_Encoded', 'J&J Role_Encoded',
            'Cost Center Sector_Encoded', 'Matter_Country_State_Encoded',
            'J&J Reporting Client Sector_Encoded', 'Matter Status_Encoded'
        ]
        X_numerical_test = X_test[numerical_columns]
        X_test_scaled = scale_data(scaler, X_numerical_test)

        # Make predictions
        y_pred = predict_model(model, X_test_scaled, scaler_target)

        # Evaluate predictions
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        logging.info(f"Model evaluation completed. R2 Score: {r2}, MSE: {mse}")
        print(f"R2 Score: {r2}, MSE: {mse}")

        # Visualize results
        plt.scatter(y_test, y_pred)
        plt.xlabel("Actual Values")
        plt.ylabel("Predicted Values")
        plt.title("Actual vs Predicted")
        plt.show()

        logging.info("Invoice cost prediction pipeline completed successfully.")
    except Exception as e:
        logging.error(f"Error in main pipeline: {str(e)}")
        raise

# Helper functions
def encode_categorical_columns(df, target_column, categorical_columns):
    try:
        logging.info("Encoding categorical columns.")
        for col in categorical_columns:
            target_mean_map = df.groupby(col)[target_column].mean().to_dict()
            df[f"{col}_Encoded"] = df[col].map(target_mean_map)
            df.drop(col, axis=1, inplace=True)
        logging.info("Categorical columns encoded successfully.")
        return df
    except Exception as e:
        logging.error(f"Error encoding categorical columns: {str(e)}")
        raise

def scale_data(scaler, df):
    try:
        logging.info("Scaling numerical data.")
        return scaler.transform(df)
    except Exception as e:
        logging.error(f"Error scaling numerical data: {str(e)}")
        raise

def predict_model(model, X_test_scaled, scaler_target):
    try:
        logging.info("Making predictions.")
        y_pred = model.predict(X_test_scaled)
        y_pred = scaler_target.inverse_transform(y_pred.reshape(-1, 1)).flatten()
        logging.info("Predictions completed successfully.")
        return y_pred
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        raise

# Entry point
if __name__ == "__main__":
    main()
