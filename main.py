import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load liquor store sales data from a CSV file.

    Parameters:
        file_path (str): The path to the CSV file containing sales data.

    Returns:
        pd.DataFrame: DataFrame containing the loaded sales data.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}.")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: No data found in the file.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def preprocess_data(df):
    """
    Preprocess the sales data by converting data types and handling missing values.

    Parameters:
        df (pd.DataFrame): The raw sales data.

    Returns:
        pd.DataFrame: Preprocessed sales data.
    """
    # Convert 'zip_code' to integer type
    if 'zip_code' in df.columns:
        df['zip_code'] = df['zip_code'].astype(int)
        print("Converted 'zip_code' to integer type.")
    else:
        print("Warning: 'zip_code' column not found in data.")

    # Handle missing values if any (example: fill with zeros)
    df.fillna({'bottles_sold': 0, 'sale_dollars': 0}, inplace=True)
    print("Filled missing values in 'bottles_sold' and 'sale_dollars' with zeros.")

    return df

def aggregate_sales_by_zip(df):
    """
    Aggregate total bottles sold per zip code.

    Parameters:
        df (pd.DataFrame): The preprocessed sales data.

    Returns:
        pd.Series: Total bottles sold per zip code.
    """
    sales_by_zip = df.groupby('zip_code')['bottles_sold'].sum().sort_values(ascending=False)
    print("Aggregated total bottles sold per zip code.")
    return sales_by_zip

def aggregate_sales_by_store(df):
    """
    Aggregate total sales dollars per store.

    Parameters:
        df (pd.DataFrame): The preprocessed sales data.

    Returns:
        pd.Series: Total sales dollars per store.
    """
    sales_by_store = df.groupby('store_name')['sale_dollars'].sum().sort_values(ascending=False)
    print("Aggregated total sales dollars per store.")
    return sales_by_store

def save_data(df, output_path):
    """
    Save the processed DataFrame to a CSV file.

    Parameters:
        df (pd.DataFrame): The processed sales data.
        output_path (str): The path to save the processed CSV file.
    """
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}.")

def visualize_sales(df):
    """
    Create a scatter plot of bottles sold vs. zip code.

    Parameters:
        df (pd.DataFrame): The preprocessed sales data.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df['zip_code'], df['bottles_sold'], alpha=0.5)
    plt.title('Bottles Sold per Zip Code')
    plt.xlabel('Zip Code')
    plt.ylabel('Bottles Sold')
    plt.grid(True)
    plt.show()
    print("Displayed scatter plot of bottles sold per zip code.")

def main():
    """
    Main function to execute the data analysis workflow.
    """
    # Define file paths
    input_file = 'data/liquorstore1.csv'
    output_file = 'data/liquorstore_output.csv'

    # Step 1: Load Data
    df = load_data(input_file)

    # Step 2: Preprocess Data
    df = preprocess_data(df)

    # Step 3: Aggregate Data
    sales_by_zip = aggregate_sales_by_zip(df)
    sales_by_store = aggregate_sales_by_store(df)

    # Step 4: Display Aggregated Results
    print("\nTotal Bottles Sold per Zip Code:")
    print(sales_by_zip)

    print("\nTotal Sales Dollars per Store:")
    print(sales_by_store)

    # Step 5: Save Processed Data
    save_data(df, output_file)

    # Step 6: (Optional) Visualize Data
    visualize = input("\nWould you like to visualize the data? (yes/no): ").strip().lower()
    if visualize == 'yes':
        visualize_sales(df)
    else:
        print("Visualization skipped.")

if __name__ == "__main__":
    main()
