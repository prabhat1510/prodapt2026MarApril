#Write a program to create a dataframe and show the dataframe using pyspark

import os
import sys
import pyspark

# 1. Fix version mismatch by forcing Spark to use internal JARs
if 'SPARK_HOME' in os.environ:
    del os.environ['SPARK_HOME']
os.environ['SPARK_HOME'] = os.path.dirname(pyspark.__file__)

# 2. Use JDK 17 for better stability on Windows
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-21'

# 3. Fix Python worker crash (EOFException) on Windows
os.environ['PYSPARK_PYTHON'] = 'python'
os.environ['PYSPARK_DRIVER_PYTHON'] = 'python'

from pyspark.sql import SparkSession
from datetime import datetime, date
from pyspark.sql import Row

# 4. Configure SparkSession for Java 17+ compatibility
java_options = "--add-opens=java.base/java.lang=ALL-UNNAMED " + \
               "--add-opens=java.base/java.lang.invoke=ALL-UNNAMED " + \
               "--add-opens=java.base/java.lang.reflect=ALL-UNNAMED " + \
               "--add-opens=java.base/java.io=ALL-UNNAMED " + \
               "--add-opens=java.base/java.net=ALL-UNNAMED " + \
               "--add-opens=java.base/java.nio=ALL-UNNAMED " + \
               "--add-opens=java.base/java.util=ALL-UNNAMED " + \
               "--add-opens=java.base/java.util.concurrent=ALL-UNNAMED " + \
               "--add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED " + \
               "--add-opens=java.base/sun.nio.ch=ALL-UNNAMED " + \
               "--add-opens=java.base/sun.nio.cs=ALL-UNNAMED " + \
               "--add-opens=java.base/sun.security.action=ALL-UNNAMED " + \
               "--add-opens=java.base/sun.util.calendar=ALL-UNNAMED " + \
               "--add-opens=java.security.jgss/sun.security.krb5=ALL-UNNAMED"

spark = SparkSession.builder \
    .appName("FundamentalTest") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.extraJavaOptions", java_options) \
    .config("spark.executor.extraJavaOptions", java_options) \
    .getOrCreate()

print("Constructing DataFrame...")
df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])

df.show()
spark.stop()