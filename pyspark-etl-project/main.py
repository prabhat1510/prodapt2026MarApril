from config.spark_config import get_spark_session
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_etl():
    spark = get_spark_session()

    orders, customers, products = extract_data(spark)
    df, revenue_df = transform_data(orders, customers, products)
    load_data(df, revenue_df)

    spark.stop()

if __name__ == "__main__":
    run_etl()