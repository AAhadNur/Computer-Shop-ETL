from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import os

# project directory
project_dir = '/home/a_ahad/Desktop/Workshop/Computer-Shop/Computer-Shop'

default_args = {
    'owner': 'Abdul Ahad',
    'start_date': datetime(2023, 11, 11),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=15),
    'max_active_runs': 1,
    'catchup': False,
}

dag = DAG(
    'my_datapipeline_dag',
    default_args=default_args,
    description='An example DAG with detailed default_args',
    schedule_interval=timedelta(days=7),
    catchup=False,
    max_active_runs=1,
    tags=['Scrapy', 'Airflow', 'ETL', 'PostgreSQL'],
)


def extract_data():
    pass


def transform_data():
    os.system(f"cd {project_dir}/TransformScripts && python transform.py")


def load_data():
    os.system(f"cd {project_dir}/LoadData && python load_data.py")


# BashOperator to execute Scrapy Ryans spiders
crawl_ryans = BashOperator(
    task_id='crawl_ryans',
    bash_command=f"cd {project_dir}/ExtractingLaptopData && scrapy crawl ryans -O RyansData.json",
    dag=dag,
)

# BashOperator to execute Scrapy Startech spiders
crawl_startech = BashOperator(
    task_id='crawl_startech',
    bash_command=f"cd {project_dir}/ExtractingLaptopData && scrapy crawl startech -O StartechData.json",
    dag=dag,
)

# Create tasks in your DAG
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

# Set up task dependencies
[crawl_ryans, crawl_startech] >> extract_task >> transform_task >> load_task
