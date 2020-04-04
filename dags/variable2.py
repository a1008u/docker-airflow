from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.models import Variable

default_args = {
    "owner": "airflow",
    "start_date": datetime(2020, 3, 30),
}

dag = DAG("variable2", default_args=default_args, schedule_interval=timedelta(1))
t1 = BashOperator(task_id="print_path", bash_command="echo {{var.value.source_path}}", dag=dag)
