---
name: databricks-mlflow-setup
description: "Create a MLflow experiment in Databricks and configure traces. Use when user wants to setup MLflow experiment within Databricks"
---

# MLflow Experiment Setup

## Prerequisites
1. An `.env` file exists in the project's root directory with the following information:
   
```
DATABRICKS_TOKEN=<databricks-personal-access-token>
DATABRICKS_HOST=https://<workspace-name>.cloud.databricks.com
MLFLOW_TRACKING_URI=databricks
MLFLOW_REGISTRY_URI=databricks-uc
```

## Process

### 1.0 Create MLflow Experiment
Here is an example on how to create an MLflow Experiment:

```python

from dotenv import load_dotenv
import mlflow   
# Load environment variables from .env file
load_dotenv()
                                                                                                   
# Create an experiment                                                                                    
experiment_id = mlflow.create_experiment(name="/Users/your-email/my-experiment")   

print(f"Experiment ID: {experiment_id}")
```

### 2.0 Update .env File
After the MLflow Experiment is created, update the the `.env` to include `MLFLOW_EXPERIMENT_ID`

The `.env` file should now look like this:
```
DATABRICKS_TOKEN=<databricks-personal-access-token>
DATABRICKS_HOST=https://<workspace-name>.cloud.databricks.com
MLFLOW_TRACKING_URI=databricks
MLFLOW_REGISTRY_URI=databricks-uc
MLFLOW_EXPERIMENT_ID=<MLFLOW EXPERIMENT ID>
```

## Next Steps
1. Ask the user to verify that the experiment is created successfully
2. Provide user with the name of the MLflow experiment that is created 