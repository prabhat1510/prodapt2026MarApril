import os
import sys

import pandas as pd
from pyspark.sql.functions import col,upper
# 1. Import your config helper
from config.spark_config import get_spark_session

# 2. Initialize Spark Session
spark = get_spark_session()

print("Extracting data...")

def extract_data(spark):
    file_path = "D:\\prodapt2026MarApril\\datasetforlabs\\telecom_churn.csv"
    telecom_df = spark.read.csv(file_path, header=True, inferSchema=True)
    return telecom_df

# transform data
def transform_data(df):
    # repartition the data
    df_repartitioned = df.repartition(10)
    # Ensure column name matches CSV exactly or handle case-insensitivity
    # CSV has 'churn', we'll standardize to 'Churn'
    df_cleaned = df_repartitioned.filter(col("churn").isNotNull())
    # converting to string for 'upper' if needed, though 'churn' is numeric (0/1)
    # If the user wants to keep it numeric, upper() is not needed. 
    # But since they had upper(col("Churn")), I'll keep the logic but ensure name consistency.
    df_processed = df_cleaned.withColumn("Churn", upper(col("churn").cast("string")))
    return df_processed

# load data
def load_data(df):
    #df.write.mode("overwrite").partitionBy("Churn").parquet("data/processed/telecom_churn")
    print("Loading data into MySQL...")
    try:
        df.write.format("jdbc") \
            .option("url", "jdbc:mysql://localhost:3306/telecom_churn_db") \
            .option("driver", "com.mysql.cj.jdbc.Driver") \
            .option("dbtable", "telecom_churn") \
            .option("user", "root") \
            .option("password", "password") \
            .mode("overwrite") \
            .save()
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading to MySQL: {e}")
        print("Falling back to local Parquet storage...")
        df.write.mode("overwrite").partitionBy("Churn").parquet("data/processed/telecom_churn")
        print("Data saved to data/processed/telecom_churn")

# Execute Pipeline
df_raw = extract_data(spark)
df_raw.show(5)

df_transformed = transform_data(df_raw)
df_transformed.show(5)

load_data(df_transformed)

spark.stop()
sys.stdout.flush()
os._exit(0)

