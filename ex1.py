import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-21'
os.environ['HADOOP_HOME'] = r'C:\hadoop'
os.environ['PATH'] = r'C:\hadoop\bin;' + os.environ['PATH']

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

tmp_dir = r'C:\tmp\spark-temp'
os.makedirs(tmp_dir, exist_ok=True)

spark = SparkSession.builder \
    .appName("TestApp") \
    .master("local[*]") \
    .config("spark.local.dir", tmp_dir) \
    .config("spark.driver.memory", "2g") \
    .config("spark.executor.memory", "2g") \
    .config("spark.sql.shuffle.partitions", "2") \
    .config("spark.driver.host", "localhost") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .config("spark.ui.enabled", "false") \
    .config("spark.python.worker.reuse", "true") \
    .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true") \
    .config("spark.python.worker.faulthandler.enabled", "true") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("✅ Spark Version:", spark.version)
print("✅ Python:", sys.executable)

schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age",  IntegerType(), True)
])

data = [("Prabhat", 25), ("Data", 30)]
df = spark.createDataFrame(data, schema=schema)
df.show()
df.printSchema()

spark.stop()
print("✅ Done.")