import os
import sys
import ctypes

# ─── CRITICAL: Remove SPARK_HOME BEFORE importing pyspark ────────────────────
# pyspark/__init__.py caches SPARK_HOME via _find_spark_home() at import time.
# System SPARK_HOME = C:\spark (Spark 4.1.1), pip pyspark = 3.5.5.
# Deleting it first forces pyspark to cache its OWN bundled 3.5.5 JARs instead.
os.environ.pop('SPARK_HOME', None)

def _short_path(long_path: str) -> str:
    """Convert a Windows long path to its 8.3 short form (removes spaces)."""
    buf = ctypes.create_unicode_buffer(260)
    ctypes.windll.kernel32.GetShortPathNameW(long_path, buf, 260)
    return buf.value or long_path

# ─── Windows environment setup ────────────────────────────────────────────────
if os.name == 'nt':
    import pyspark  # imported AFTER SPARK_HOME is removed — uses bundled JARs

    # 1. Python executable — short (8.3) path to avoid spaces in "UD SYSTEMS"
    #    which would cause "Missing Python executable" in Spark worker spawn.
    py_short = _short_path(sys.executable)
    os.environ['PYSPARK_PYTHON']        = py_short
    os.environ['PYSPARK_DRIVER_PYTHON'] = py_short

    # 2. UTF-8 encoding — prevents UnicodeEncodeError in worker stdout.
    os.environ['PYTHONUTF8']       = '1'
    os.environ['PYTHONIOENCODING'] = 'utf-8'

    # 3. Append pyspark's site-packages parent to PYTHONPATH (don't overwrite).
    pyspark_parent = os.path.dirname(os.path.dirname(pyspark.__file__))
    existing_pp    = os.environ.get('PYTHONPATH', '')
    os.environ['PYTHONPATH'] = (
        pyspark_parent + os.pathsep + existing_pp if existing_pp else pyspark_parent
    )

    # 4. JAVA_HOME — short path to avoid spaces in "Program Files".
    os.environ['JAVA_HOME'] = 'C:/PROGRA~1/Java/jdk-17'

    # 5. HADOOP_HOME / winutils.
    hadoop_home = os.environ.get('HADOOP_HOME', 'C:/spark')
    os.environ['HADOOP_HOME'] = hadoop_home
    os.environ['PATH'] = (
        os.path.join(hadoop_home, 'bin') + os.pathsep + os.environ.get('PATH', '')
    )

    # 6. Spark scratch dir — on D: drive, short/space-free path.
    # Set SPARK_LOCAL_DIRS to a path without spaces
    #tmp_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp')
    tmp_dir='D:/prodapt2026MarApril/pysparkfundamentals/tmp'
    os.environ['SPARK_LOCAL_DIRS'] = tmp_dir

# ─── Imports ──────────────────────────────────────────────────────────────────
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# ─── SparkSession factory ──────────────────────────────────────────────────────
def get_spark_session() -> SparkSession:
    """Return a SparkSession tuned for Windows + JDK 17."""
    jvm_opts = (
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
    return (
        SparkSession.builder
        .appName("Ecommerce_ETL")
        .master("local[1]")
        .config("spark.driver.extraJavaOptions",  jvm_opts)
        .config("spark.executor.extraJavaOptions", jvm_opts)
        .config("spark.hadoop.fs.file.impl",  "org.apache.hadoop.fs.RawLocalFileSystem")
        .config("spark.driver.host",          "127.0.0.1")
        .config("spark.driver.bindAddress",   "127.0.0.1")
        .config("spark.sql.execution.arrow.pyspark.enabled",            "false")
        .config("spark.python.worker.reuse",                            "false")
        .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true")
        .config("spark.python.worker.faulthandler.enabled", "true")
        .getOrCreate()
    )

# ─── Main ──────────────────────────────────────────────────────────────────────
spark = get_spark_session()
print("SparkSession Created Successfully")

# schema = StructType([
#     StructField("id",   IntegerType(), nullable=False),
#     StructField("name", StringType(),  nullable=False),
#     StructField("age",  IntegerType(), nullable=False),
# ])

# data = [
#     (1, "Prabhat", 28),
#     (2, "Rahul",   25),
#     (3, "Anjali",  27),
# ]
df = spark.createDataFrame([(1, 'Alice'), (2, 'Bob')], ['id', 'name'])


 # Safe Debugging
print("👉 DataFrame Object:", df)
print("👉 Columns:", df.columns)
print("👉 Schema:")
df.printSchema()

print("👉 Explain Plan:")
df.explain()

print("👉 Show Data:")
df.show()

print("👉 Count:")
print(df.count())

spark.stop()
print("✅ Spark Stopped")