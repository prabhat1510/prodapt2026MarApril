import pandas as pd

# EXTRACT
df = pd.read_csv("sales.csv")
print("Raw Data:\n", df)

# TRANSFORM
df["revenue"] = df["price"] * df["quantity"]

# LOAD
df.to_csv("processed_sales.csv", index=False)

print("\nProcessed Data:\n", df)