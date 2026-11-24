
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


### Question 4:  
B. Airflow can orchestrate dbt commands while dbt manages transformation logic.


### Question 7: 

Goal: Recognize the reasons teams package dbt execution into a container image.
A — Useful: pinning the image and dependencies helps keep environments consistent.
B — Not useful: image versions should be documented and controlled.
C — Useful: the image packages dbt and its dependencies together.
D — Not useful: containers do not remove the need for credentials, permissions, network connectivity, or access to data.
Suggested answers: A useful; B not useful; C useful; D not useful.


### Q8 — MCQ: Separate Run and Test Tasks
Goal: Understand why separate Airflow tasks can improve observability.
Correct answer: C. They make it easier to identify whether model execution or testing failed.