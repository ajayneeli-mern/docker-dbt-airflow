from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('example_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='dbt run'
        #bash_command='echo hello ajay'
    )

run_dbt
