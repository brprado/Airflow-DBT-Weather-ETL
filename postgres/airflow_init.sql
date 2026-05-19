-- Executado só na primeira inicialização do volume Postgres (docker-entrypoint-initdb.d).
CREATE USER airflow WITH PASSWORD 'airflow';
CREATE DATABASE airflow_db OWNER airflow;
