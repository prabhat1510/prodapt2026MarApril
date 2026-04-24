def load_data(df, revenue_df):
    df.write.mode("overwrite").parquet("data/processed/full_data")
    revenue_df.write.mode("overwrite").parquet("data/processed/revenue_per_customer")