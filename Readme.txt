project/
├── dags/
│   └── example_dag.py
├── dbt/
│   ├── dbt_project.yml
│   ├── models/
│   │   └── example_model.sql
│   ├── profiles.yml
├── logs/
├── plugins/
├── docker-compose.yml

http://localhost:8080   ->airflow

http://localhost:5050   ->pgadmin




docker-compose up -d 
docker exec -it docker-dbt-airflow-dbt-1 /bin/bash

docker exec -it docker-dbt-airflow_dbt_1 /bin/bash
cd /usr/app/dbt
  ->here exec dbt scripts

dbt run

postgres

docker-dbt-airflow-postgres-1

docker exec -it docker-dbt-airflow-postgres-1 psql -U airflow -d airflow

-- Inside the psql shell
\dt

-- or to check for a specific table
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'airflow'
AND table_name = 'ajay';
