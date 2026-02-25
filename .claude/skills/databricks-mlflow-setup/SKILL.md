---
name: databricks-mlflow-setup
description: "Create a MLflow experiment in Databricks and configure traces to be sent to a Unity Catalog Schema. Use when user wants to setup MLflow experiment within Databricks"
---

# MLflow Experiment Setup

## Prerequisites
1. Ensure that the [OpenTelemetry on Databricks preview feature](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog) is enabled in the workspace
2. Ensure that the you have access to a Databricks SQL Warehouse
3. Created a .env file with the following:
   
```
DATABRICKS_TOKEN=<databricks-personal-access-token>
DATABRICKS_HOST=https://<workspace-name>.cloud.databricks.com
MLFLOW_TRACKING_URI=databricks
MLFLOW_REGISTRY_URI=databricks-uc
MLFLOW_TRACING_SQL_WAREHOUSE_ID=<SQL_WAREHOUSE_ID>
MLFLOW_TRACING_DESTINATION=<catalog.schema> # Replace with your schema
```

## Process

### 1.0 Code Execution
Execute the following sample script with the correct parameters:

```python
# Example values for the placeholders below:
# MLFLOW_TRACING_SQL_WAREHOUSE_ID: "abc123def456" (found in SQL warehouse URL)
# experiment_name: "/Users/user@company.com/traces"
# catalog_name: "main" or "my_catalog"
# schema_name: "mlflow_traces" or "production_traces"

import os
import mlflow
from mlflow.exceptions import MlflowException
from mlflow.entities import UCSchemaLocation
from mlflow.tracing.enablement import set_experiment_trace_location
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mlflow.set_tracking_uri("databricks")

# Specify the ID of a SQL warehouse you have access to.
os.environ["MLFLOW_TRACING_SQL_WAREHOUSE_ID"] = "<SQL_WAREHOUSE_ID>"
# Specify the name of the MLflow Experiment to use for viewing traces in the UI.
experiment_name = "<MLFLOW_EXPERIMENT_NAME>"
# Specify the name of the Catalog to use for storing traces.
catalog_name = "<UC_CATALOG_NAME>"
# Specify the name of the Schema to use for storing traces.
schema_name = "<UC_SCHEMA_NAME>"

if experiment := mlflow.get_experiment_by_name(experiment_name):
    experiment_id = experiment.experiment_id
else:
    experiment_id = mlflow.create_experiment(name=experiment_name)
print(f"Experiment ID: {experiment_id}")

# To link an experiment to a trace location
result = set_experiment_trace_location(
    location=UCSchemaLocation(catalog_name=catalog_name, schema_name=schema_name),
    experiment_id=experiment_id,
)
print(result.full_otel_spans_table_name)
```

## Next Steps
Ask the user to verify that the tables are created in their schema:
- mlflow_experiment_trace_otel_logs
- mlflow_experiment_trace_otel_metrics
- mlflow_experiment_trace_otel_spans