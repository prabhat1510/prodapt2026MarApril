
from pyspark.sql import SparkSession

from pyspark.sql.functions import col, sum, avg, count, when, upper, to_date

# 1. Initialize Spark Session 
spark = SparkSession.builder \
                    .appName("SalesDataPipeline") \
                    .getOrCreate() 
# 2. Extract: Load raw sales data (Sample data creation) 
data = [ ("Store1", "2023-01-01", "Laptop", 1200.0, 2), ("Store2", "2023-01-02", "mouse", 50.0, None),("Store3", "2023-01-03", None, 0.0, 1),("Store2", "2023-01-04", "Mouse", 55.0, 5) ]     
        # Missing quantity ("Store1", "2023-01-02", "LAPTOP", 1200.0, 1), 
        #  Mixed casing ("Store3", "2023-01-03", None, 0.0, 1), 
        # Null product ("Store2", "2023-01-04", "Mouse", 55.0, 5) ] 
columns = ["store_id", "sale_date", "product_name", "price", "quantity"] 

df = spark.createDataFrame(data, columns)

# 3. Clean: Handle nulls, standardize text, and cast types 
cleaned_df = df.filter(col("product_name").isNotNull())\
	          .withColumn("product_name", upper(col("product_name")))\
                           .withColumn("sale_date", to_date(col("sale_date")))\
	          .na.fill({"quantity": 0}) # Fill missing quantity with 0
# 4. Aggregate: Group by store and product to find total revenue # Revenue = price * quantity
processed_df = cleaned_df.withColumn("revenue", col("price") * col("quantity")) \
                 .groupBy("store_id", "product_name") \
                 .agg( sum("revenue").alias("total_revenue"), avg("price").alias("avg_unit_price"), count("product_name").alias("transaction_count") )
processed_df.show()
# 5. Store: Save results to Parquet for efficient storage
output_path = "processed_sales_data" 
processed_df.write.mode("overwrite").parquet(output_path)
