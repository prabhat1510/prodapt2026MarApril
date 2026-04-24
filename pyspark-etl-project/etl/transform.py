from pyspark.sql.functions import col, sum as _sum,broadcast

def transform_data(orders, customers, products):
    
    # Join datasets
    df = orders.join(customers, "customer_id") \
               .join(broadcast(products), "product_id")

    # Clean data
    df = df.dropDuplicates()

    # Convert amount to numeric (if needed)
    df = df.withColumn("amount", col("amount").cast("double"))

    # Business aggregation
    revenue_per_customer = df.groupBy("name", "city") \
                             .agg(_sum("amount").alias("total_spent"))

    return df, revenue_per_customer