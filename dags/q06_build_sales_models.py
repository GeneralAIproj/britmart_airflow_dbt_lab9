from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
DBT = "/home/YOUR_LINUX_USER/britmart-airflow-dbt-lab/.venv/bin/dbt"
PROJECT = "/home/YOUR_LINUX_USER/britmart-airflow-dbt-lab/britmart_pipeline_dbt"
PROFILES = "/home/YOUR_LINUX_USER/.dbt"
with DAG(
    dag_id="q06_build_sales_models",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
 build_sales_models = BashOperator(
    task_id="build_sales_models",
    bash_command=(
    f"{DBT} build --select +fct_daily_sales "
    f"--project-dir {PROJECT} --profiles-dir {PROFILES}"
    ),
 )