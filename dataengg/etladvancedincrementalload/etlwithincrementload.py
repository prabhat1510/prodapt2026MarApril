#Only load new data (like production pipelines)
import pandas as pd

# Existing data
existing_df = pd.read_csv("../processed_sales.csv")

# New data
new_df = pd.read_csv("../new_sales.csv")

# TRANSFORM
new_df["revenue"] = new_df["price"] * new_df["quantity"]

# Incremental logic (avoid duplicates)
final_df = pd.concat([existing_df, new_df]).drop_duplicates(subset=["order_id"])

# LOAD
final_df.to_csv("../processed_sales.csv", index=False)

print("Incremental load complete")