import os
import sys
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
# 1. Import your config helper
from config.spark_config import get_spark_session

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