#PRODUCTION-STYLE ETL (Logging + Error Handling)
import logging

logging.basicConfig(filename="etl.log", level=logging.INFO)

def extract():
    try:
        df = pd.read_csv("sales.csv")
        logging.info("Extract success")
        return df
    except Exception as e:
        logging.error(f"Extract failed: {e}")
        return None

def transform(df):
    try:
        df["revenue"] = df["price"] * df["quantity"]
        logging.info("Transform success")
        return df
    except Exception as e:
        logging.error(f"Transform failed: {e}")
        return None

def load(df):
    try:
        df.to_csv("processed_sales.csv", index=False)
        logging.info("Load success")
    except Exception as e:
        logging.error(f"Load failed: {e}")

# Run ETL
df = extract()
if df is not None:
    df = transform(df)
    if df is not None:
        load(df)