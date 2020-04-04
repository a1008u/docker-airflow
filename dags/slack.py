import utils.slack_notification

from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator
from airflow.operators.python_operator import PythonOperator



default_args = {
  'start_date': datetime(2020, 4, 4),
  'on_success_callback': utils.slack_notification.success,
  'on_failure_callback': utils.slack_notification.fail,
  "owner": "airflow",
  #   "depends_on_past": False,
  #   "start_date": airflow.utils.dates.days_ago(1),
  #   "retries": 1,
  #   "on_failure_callback": slack_noti,
  #   "retry_delay": timedelta(minutes=1)
}

def success_py():
    # 1/0
    return 'success'

def fail_py():
    1/0
    return 'fail'

with DAG("slack_dag", default_args=default_args, catchup=False, schedule_interval="@daily") as dag:
  sp = PythonOperator(
      task_id='success_py',
      python_callable=success_py,
      dag=dag,
  )

  sp2 = PythonOperator(
    task_id='success2_py',
    python_callable=success_py,
    dag=dag,
  )

  fp = PythonOperator(
    task_id='fail_py',
    python_callable=fail_py,
    dag=dag,
  )

sp >> sp2 >> fp