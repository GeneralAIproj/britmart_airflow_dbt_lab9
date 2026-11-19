
#!/usr/bin/env bash

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source "$PROJECT_DIR/.venv/bin/activate"

export AIRFLOW_HOME="$PROJECT_DIR/.airflow"
export AIRFLOW__CORE__DAGS_FOLDER="$PROJECT_DIR/dags"

echo "BritMart environment activated"
echo "AIRFLOW_HOME=$AIRFLOW_HOME"

