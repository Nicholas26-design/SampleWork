# import needed libraries
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os
import yfinance as yf




"""

Extract

"""

print(os.getcwd())  # Prints the current working directory






class ETLProcess:
    def __init__(self, csv_file, db_uri):
        self.csv_file = csv_file
        self.db_uri = db_uri

    def extract(self):
        # Extract the data
        try:
            aapl = yf.Ticker("AAPL")
            # get all stock info
            aapl.info
            # get historical market data
            hist = aapl.history(period="5y")
            # download sample data
            os.chdir("C:\\Users\\NicholasKenney\\PycharmProjects\\ETL Pipeline\\Sample Data")
            df = pd.DataFrame(hist)
            df.to_csv('AAPL.csv')
            # Extract data from the CSV file into a DataFrame
            self.data = pd.read_csv(self.csv_file)
            print("Data extracted successfully.")
        except Exception as e:
            print(f"Error during data extraction: {str(e)}")

    def transform(self):
        # Transform the data
        try:
            # Making columns lowercase.
            self.data.columns = [col.lower() for col in self.data.columns]
            df = pd.DataFrame(self.data)
            # Drop columns based on column index.
            df_new = df.drop(df.columns[[2, 3, 4]], axis=1)
            print(df_new)
        except Exception as e:
            print(f"Error occurred during transformation: {str(e)}")

    def load(self):
        # Load the data
        try:
            # Load the transformed data into a database
            engine = create_engine(self.db_uri)
            self.data.to_sql('stock_info', engine, if_exists='replace', index=False)
            print("Data loaded into the database successfully.")
            # Load the data into a graph
        except Exception as e:
            print(f"Error during data loading: {str(e)}")

    def run_etl(self):
        # Execute the complete ETL process
        self.extract()
        self.transform()
        self.load()


# Example usage:
if __name__ == "__main__":
    csv_file = 'AAPL.csv'
    db_uri = 'sqlite:///your_database.db'  # SQLite example, you can use other database URIs

    etl_process = ETLProcess(csv_file, db_uri)
    etl_process.run_etl()