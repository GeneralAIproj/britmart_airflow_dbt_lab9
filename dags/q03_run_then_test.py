from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
DBT = "/home/YOUR_LINUX_USER/britmart-airflow-dbt-lab/.venv/bin/dbt"
PROJECT = "/home/YOUR_LINUX_USER/britmart-airflow-dbt-lab/britmart_pipeline_dbt"

PROFILES = "/home/YOUR_LINUX_USER/.dbt"
COMMON = f"--project-dir {PROJECT} --profiles-dir {PROFILES}"
with DAG(
    dag_id="q03_run_then_test",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    ) as dag:
        dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"{DBT} run --select marts {COMMON}",
    )
dbt_test = BashOperator(
    task_id="dbt_test",
    bash_command=f"{DBT} test --select marts {COMMON}",
    )

dbt_run >> dbt_test
