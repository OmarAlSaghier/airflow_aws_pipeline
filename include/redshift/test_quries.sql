--  Select from 'retail' table
SELECT * FROM retail;

-- Manual insert into 'retail' table for testing
INSERT INTO retail VALUES (536365,'85123A','WHITE HANGING HEART T-LIGHT HOLDER',6,'12/1/10 8:26',2.55,17850,'United Kingdom');

-- COPY s3 files into 'retail' table for testing
COPY dev.public.retail 
FROM 's3://airflow-end-to-end/online_retail.csv' 
IAM_ROLE 'arn:aws:iam::088061495104:role/redshiftCopyRole' 
FORMAT AS CSV 
DELIMITER ',' 
QUOTE '"' 
IGNOREHEADER 1
REGION AS 'us-east-1';

-- for inspecting the errors
SELECT * FROM sys_load_error_detail;
