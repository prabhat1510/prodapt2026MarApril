from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
# 1. Import your config helper
import os
import sys
from pyspark.sql import SparkSession

# Windows-specific configuration
if os.name == 'nt':
    import pyspark
    # Set Python path for Spark workers to match the current interpreter
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
    os.environ['PYTHONPATH'] = os.path.dirname(os.path.dirname(pyspark.__file__))
    
    # Set JAVA_HOME to short path to avoid issues with spaces (Program Files)
    os.environ['JAVA_HOME'] = "C:/Program Files/Java/jdk-17"
    
    # Default HADOOP_HOME to C:/spark if not already set
    hadoop_home = os.environ.get('HADOOP_HOME', "C:/spark")
    os.environ['HADOOP_HOME'] = hadoop_home
    os.environ['PATH'] = os.path.join(hadoop_home, 'bin') + os.path.pathsep + os.environ['PATH']
    
    # Set SPARK_LOCAL_DIRS to a path without spaces
    tmp_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp')
    os.environ['SPARK_LOCAL_DIRS'] = tmp_dir
    
    # Ensure SPARK_HOME is unset to use the pyspark-bundled JARs
    if 'SPARK_HOME' in os.environ:
        del os.environ['SPARK_HOME']

def get_spark_session():
    # JVM options for compatibility with JDK 17+
    jvm_options = (
        "--add-opens=java.base/java.lang=ALL-UNNAMED "
        "--add-opens=java.base/java.lang.invoke=ALL-UNNAMED "
        "--add-opens=java.base/java.io=ALL-UNNAMED "
        "--add-opens=java.base/java.net=ALL-UNNAMED "
        "--add-opens=java.base/java.nio=ALL-UNNAMED "
        "--add-opens=java.base/java.util=ALL-UNNAMED "
        "--add-opens=java.base/java.util.concurrent=ALL-UNNAMED "
        "--add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED "
        "--add-opens=java.base/sun.nio.ch=ALL-UNNAMED "
        "--add-opens=java.base/sun.nio.cs=ALL-UNNAMED "
        "--add-opens=java.base/sun.security.action=ALL-UNNAMED "
        "--add-opens=java.base/sun.util.calendar=ALL-UNNAMED "
        "--add-opens=java.security.sasl/com.sun.security.sasl=ALL-UNNAMED"
    )

    return SparkSession.builder \
        .appName("Ecommerce_ETL") \
        .master("local") \
        .config("spark.driver.extraJavaOptions", jvm_options) \
        .config("spark.executor.extraJavaOptions", jvm_options) \
        .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.RawLocalFileSystem") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
        .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true") \
        .getOrCreate()

# 2. Use the helper instead of SparkSession.builder
spark = get_spark_session()

print("Constructing DataFrame...")
pandas_df = pd.DataFrame({
   'a': [1, 2, 4],
   'b': [2., 3., 5.],
   'c': ['string1', 'string2', 'string3'],
   'd': [date(2000, 1, 1), date(2000, 2, 1), date(2000, 3, 1)],
   'e': [datetime(2000, 1, 1, 12, 0), datetime(2000, 1, 2, 12, 0), datetime(2000, 1, 3, 12, 0)]
})

df = spark.createDataFrame(pandas_df)
print(df)
df.show()

spark.stop()
sys.stdout.flush()
os._exit(0)