#BIG DATA ETL (PYSPARK)
#Scenario
#Handle millions/billions of records

#pip install pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL").getOrCreate()

# EXTRACT
df = spark.read.csv("sales.csv", header=True, inferSchema=True)

# TRANSFORM
# df["revenue"] = df["price"] * df["quantity"]
df = df.withColumn("revenue", df.price * df.quantity)

# LOAD
df.write.mode("overwrite").csv("output")

df.show()