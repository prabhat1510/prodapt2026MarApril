#ENTERPRISE ETL (AIRFLOW STYLE PIPELINE)
#Schedule & orchestrate ETL jobs

#Airflow DAG Example

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

def etl():
    df = pd.read_csv("../sales.csv")
    df["revenue"] = df["price"] * df["quantity"]
    df.to_csv("../output.csv", index=False)

default_args = {"start_date": datetime(2024, 1, 1)}

with DAG("etl_pipeline", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    task = PythonOperator(
        task_id="run_etl",
        python_callable=etl
    )