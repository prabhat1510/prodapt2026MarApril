import os
import sys
from pyspark.sql import SparkSession

os.environ['PYSPARK_PYTHON'] = f'"{sys.executable}"'
os.environ['PYSPARK_DRIVER_PYTHON'] = f'"{sys.executable}"'

java_options = "--add-opens=java.base/java.lang=ALL-UNNAMED " + \
               "--add-opens=java.base/java.nio=ALL-UNNAMED " + \
               "--add-opens=java.base/java.util=ALL-UNNAMED " + \
               "--add-opens=java.base/sun.nio.ch=ALL-UNNAMED"

os.environ['_JAVA_OPTIONS'] = java_options
os.environ['JAVA_OPTS'] = java_options

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SimpleTest") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.extraJavaOptions", java_options) \
    .config("spark.executor.extraJavaOptions", java_options) \
    .getOrCreate()

print("Spark Session Created")
df = spark.createDataFrame([(1, "foo"), (2, "bar")], ["id", "val"])
df.show()
spark.stop()
