from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
DBT = "/home/YOUR_LINUX_USER/britmart-airflow-dbt-lab/.venv/bin/dbt"
PROJECT = "/home/YOUR_LINUX_USER/britmart-airflow-dbt-lab/britmart_pipeline_dbt"
PROFILES = "/home/YOUR_LINUX_USER/.dbt"

with DAG(
        dag_id="q02_run_dbt",
        start_date=datetime(2025, 1, 1),
        schedule=None,
        catchup=False,
    ) as dag:
        run_dbt = BashOperator(
            task_id="run_dbt",
            bash_command=(
            f"{DBT} run --select fct_daily_sales "
            f"--project-dir {PROJECT} --profiles-dir {PROFILES}"
    ),
)