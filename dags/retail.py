from airflow.decorators import dag, task
from datetime import datetime

from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator

STARTING_DATE = datetime(2023, 9, 3)
S3_BUCKET = 'airflow-end-to-end'
REDSHIFT_TABLE='retail'
AWS_CONN_ID = 'aws'
REDSHIFT_CONN_ID = 'redshift_conn_id'

@dag(
    start_date=STARTING_DATE,
    schedule=None,
    catchup=False,
    tags=['retail'],
)
def retail():
    upload_csv_to_aws_s3 = LocalFilesystemToS3Operator(
        task_id='upload_csv_to_aws_s3',
        filename='/usr/local/airflow/include/dataset/online_retail.csv',
        dest_key='online_retail.csv',
        dest_bucket=S3_BUCKET,
        aws_conn_id=AWS_CONN_ID,
        replace=True
    )

retail()




