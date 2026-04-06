import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def extract(file):
    try:
        df = pd.read_csv(file)
        logging.info("Extraction successful")
        return df
    except Exception as e:
        logging.error(f"Extraction failed: {e}")

def transform(df):
    try:
        df["revenue"] = df["price"] * df["quantity"]
        logging.info("Transformation successful")
        return df
    except Exception as e:
        logging.error(f"Transformation failed: {e}")

def load(df, output):
    try:
        df.to_csv(output, index=False)
        logging.info("Load successful")
    except Exception as e:
        logging.error(f"Load failed: {e}")

# Pipeline
df = extract("sales.csv")
df = transform(df)
load(df, "processed_sales.csv")