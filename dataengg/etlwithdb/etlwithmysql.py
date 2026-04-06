import pandas as pd
from sqlalchemy import create_engine

# DB Connection
engine = create_engine("mysql+pymysql://root:password@localhost:3306/sales_db")

# EXTRACT
df = pd.read_csv("../sales.csv")

# TRANSFORM 
df["revenue"] = df["price"] * df["quantity"]

# LOAD
df.to_sql("sales_data", engine, if_exists="replace", index=False)

print("Data loaded into MySQL")