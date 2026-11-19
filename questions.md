
# BritMart — Airflow and dbt Integration Lab

## Part 1 — Airflow and dbt Responsibilities

### Question 1 — Choose the Right Tool

| Requirement | Tool |
|---|---|
| Schedule a daily workflow | |
| Build a SQL transformation model | |
| Run a dbt test after a dbt model | |
| Show task failure and retry state | |
| Define model lineage with ref() | |

### Question 2 — Build an Airflow Task that Runs dbt

Implementation: `dags/britmart_dbt_run.py`

### Question 3 — Separate Run and Test Tasks

Implementation: `dags/britmart_dbt_run_test.py`

