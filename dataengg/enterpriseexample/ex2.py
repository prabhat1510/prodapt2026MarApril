#Pipeline Flow:
#Source → Kafka → Spark Streaming → Data Lake (S3) → Warehouse (Snowflake/BigQuery)
#Streaming ETL Example
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StreamingETL").getOrCreate()

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sales_topic") \
    .load()

df_transformed = df.selectExpr("CAST(value AS STRING)")

query = df_transformed.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()