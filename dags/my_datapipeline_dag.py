
"""
Airflow DAG for an ETL Data Pipeline

This Python script defines an Apache Airflow Directed Acyclic Graph (DAG) for a data pipeline
that performs ETL (Extract, Transform, Load) operations. It uses various Airflow operators
and Python functions to carry out these tasks.

DAG Information:
- Name: my_datapipeline_dag
- Description: An example DAG with detailed default_args for an ETL data pipeline.
- Schedule: Runs every 7 days.
- Tags: Scrapy, Airflow, ETL, PostgreSQL

DAG Tasks:
- 'crawl_ryans' and 'crawl_startech' are BashOperators that execute Scrapy spiders.
- 'extract_data', 'transform_data', and 'load_data' are PythonOperators that execute custom Python functions.

Dependencies:
- 'crawl_ryans' and 'crawl_startech' run first, followed by 'extract_data'.
- 'extract_data' is followed by 'transform_data', and 'transform_data' is followed by 'load_data'.

Additional Information:
- The 'extract_data' function is a placeholder and should be implemented to perform data extraction.
- The 'transform_data' function runs a Python script to transform data located in the 'TransformScripts' directory.
- The 'load_data' function runs a Python script to load data located in the 'LoadData' directory.

Note: Make sure to customize the paths and scripts as needed for your specific project.

Author: Abdul Ahad
Start Date: November 11, 2023
Depends on Past Runs: False
Retries: 3
Retry Delay: 15 minutes
Max Active Runs: 1
Catchup: False
"""

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
    'retry_delay': timedelta(minutes=1),
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
