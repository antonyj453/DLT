venv = dlt.dbt.get_venv(pipeline)
dbt = dlt.dbt.package(
    pipeline,
    "https://github.com/dbt-labs/jaffle_shop.git",
    venv=venv
)
models_info = dbt.run_all()

# Load metadata for monitoring and load package lineage.
# This allows for both row and column level lineage,
# as it contains schema update info linked to the loaded data
pipeline.run([load_info], table_name="loading_status", write_disposition='append')
pipeline.run([models_info], table_name="transform_status", write_disposition='append')
