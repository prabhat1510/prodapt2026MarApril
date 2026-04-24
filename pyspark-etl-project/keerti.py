import os
import sys
 
import pandas as pd
from pyspark.sql.functions import col, sum as spark_sum, avg, count, upper, to_date
 
# 1. Import your config helper
from config.spark_config import get_spark_session
 
# 2. Initialize Spark Session
spark = get_spark_session()
 
print("Extracting data...")
# Create sampling data using Pandas (more robust for Windows PySpark workers)
pandas_data = {
    "store_id": ["Store1", "Store2", "Store3", "Store2"],
    "sale_date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
    "product_name": ["Laptop", "mouse", None, "Mouse"],
    "price": [1200.0, 50.0, 0.0, 55.0],
    "quantity": [2.0, None, 1.0, 5.0]
}
pdf = pd.DataFrame(pandas_data)
 
# Convert to Spark DataFrame
df = spark.createDataFrame(pdf)
 
print("Transforming data...")
 
# 3. Clean: Handle nulls, standardize text, and cast types
cleaned_df = (
    df.filter(col("product_name").isNotNull())
    .withColumn("product_name", upper(col("product_name")))
    .withColumn("sale_date", to_date(col("sale_date")))
    .na.fill({"quantity": 0})
)
 
# 4. Aggregate: Group by store and product to find total revenue
processed_df = (
    cleaned_df.withColumn("revenue", col("price") * col("quantity"))
    .groupBy("store_id", "product_name")
    .agg(
        spark_sum("revenue").alias("total_revenue"),
        avg("price").alias("avg_unit_price"),
        count("product_name").alias("transaction_count")
    )
)
 
print("Displaying results:")
processed_df.show()
 
# 5. Store: Save results to Parquet (Optional)
# output_path = "processed_sales_data"
# processed_df.write.mode("overwrite").parquet(output_path)
 
spark.stop()
sys.stdout.flush()
os._exit(0)