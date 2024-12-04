import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import StandardScaler

# Configure logging
logging.basicConfig(
    filename="matter_processing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Function to load data
def load_data(filepath, chunksize=None, sep='^', encoding='ISO-8859-1'):
    try:
        if chunksize:
            logging.info(f"Loading data from {filepath} in chunks.")
            data = pd.DataFrame()
            for chunk in pd.read_csv(filepath, chunksize=chunksize, sep=sep, encoding=encoding, low_memory=False):
                data = pd.concat([data, chunk], ignore_index=True)
            return data
        else:
            logging.info(f"Loading data from {filepath}.")
            return pd.read_csv(filepath, sep=sep, encoding=encoding, low_memory=False)
    except Exception as e:
        logging.error(f"Error loading data from {filepath}: {str(e)}")
        raise

# Function to preprocess data
def preprocess_data(df):
    try:
        logging.info("Starting data preprocessing.")
        
        # Filtering data
        df = df[df["Matter Type"] != "Product Liability"]
        df["Matter_Country_State"] = (
            df["Matter Country Cd"].astype(str) + ":" + df["Matter State Name"].astype(str)
        )
        
        # Adding calculated fields
        df["Matter Ages"] = (
            df["Budget_Year"].astype(int) - df["Opened On (Date)"].astype(int) + 1
        )
        df["created_year"] = pd.to_datetime(df["Matter Created Date"], errors="coerce").dt.year
        df["created_month"] = pd.to_datetime(df["Matter Created Date"], errors="coerce").dt.month
        
        # Fixing missing values
        df["Matter Status"] = df["Matter Status"].replace("?", "Open").replace("Closed", "Open")
        df["Matter_Country_State"] = df["Matter_Country_State"].replace(0, "Not Given")
        
        logging.info("Data preprocessing completed successfully.")
        return df
    except Exception as e:
        logging.error(f"Error during data preprocessing: {str(e)}")
        raise

# Function to encode categorical columns
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

# Function to scale numerical data
def scale_data(scaler, df, columns):
    try:
        logging.info("Scaling numerical data.")
        scaled_data = scaler.transform(df[columns])
        logging.info("Numerical data scaled successfully.")
        return scaled_data
    except Exception as e:
        logging.error(f"Error scaling numerical data: {str(e)}")
        raise

# Function to make predictions
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

# Main function
def main():
    try:
        # Load data
        logging.info("Starting the data processing pipeline.")
        matters_filepath = "/mnt/data/legal/matter_data/Matters.txt"
        budget_filepath = "/mnt/data/legal/matter_data/Matter Budget.txt"
        invoice_filepath = "/mnt/data/legal/invoice_data/Invoiceheaders_remove_lineend.txt"

        matters = load_data(matters_filepath, chunksize=1000)
        matter_budget = load_data(budget_filepath)
        invoice_header = load_data(invoice_filepath)

        # Preprocess data
        matters = preprocess_data(matters)

        # Prepare test data
        test = matters[matters["type"] == "test"]
        X_test = test.drop("Target_year", axis=1)
        y_test = test["Target_year"]

        # Encode categorical columns
        categorical_columns = [
            'Subject Area', 'Matter Type', 'J&J Role', 'Cost Center Sector', 
            'Action Type', 'Matter_Country_State', 'J&J Reporting Client Sector', 'Matter Status'
        ]
        X_test["Matter_Country_State"] = X_test["Matter_Country_State"].replace([np.inf, -np.inf], "Not Given")
        X_test = encode_categorical_columns(X_test, "Target_year", categorical_columns)

        # Scale numerical data
        numerical_columns = [
            'lifetime_budget', 'lifetime_invoice_cost', 'max_budget', 'average_budget', 
            'ratio_max_average_invoice_cost', 'last_year_budget', 'last_year_invoice_cost',
            'Subject Area_Encoded', 'Matter Type_Encoded', 'J&J Role_Encoded',
            'Cost Center Sector_Encoded', 'Matter_Country_State_Encoded', 
            'J&J Reporting Client Sector_Encoded', 'Matter Status_Encoded'
        ]
        scaler = StandardScaler()
        X_test_scaled = scale_data(scaler, X_test, numerical_columns)

        # Load pre-trained model and scaler for the target
        # Example: Replace with actual model and scaler
        model = None  # Load your model here
        scaler_target = None  # Load your target scaler here

        # Make predictions
        y_pred = predict_model(model, X_test_scaled, scaler_target)
        print("Predictions:", y_pred)

        logging.info("Data processing pipeline completed successfully.")
    except Exception as e:
        logging.error(f"Error in main pipeline: {str(e)}")
        raise

# Entry point
if __name__ == "__main__":
    main()
