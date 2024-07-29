
  create view "airflow"."airflow"."example_model__dbt_tmp"
    
    
  as (
    -- example_model.sql
select 1 as id, 'example' as name
  );