# Get Started

### Requirements
Ensure you have Python 3.11 or above

Create a vitrual environment in the project directory:

```
python -m venv .venv
```

Activate the virtual environment:
```
source .venv/bin/activate
```

Install the required Python libraries:
```
pip install -r requirements.txt
```

### For Codex Only
Run the following script to copy files over to `.agents` folder

```bash
python lab_setup/scripts/initialization/setup_codex.py
```

### Databricks CLI
Ensure that you have the latest version of Databricks CLI install. Refer to this [documentation](https://docs.databricks.com/aws/en/dev-tools/cli/install) for more details

### Setup Databricks Profile 
Run the following command to authenticate and set up a Databricks Profile for your workspace:
```
databricks auth login <workspace-url>
```

### Install ai-dev-kit
Install [ai-dev-kit](https://github.com/databricks-solutions/ai-dev-kit/tree/main) by running the following command in the project directory:

Mac user:
```
bash <(curl -sL https://raw.githubusercontent.com/databricks-solutions/ai-dev-kit/main/install.sh)
```

Windows user:
```
irm https://raw.githubusercontent.com/databricks-solutions/ai-dev-kit/main/install.ps1 | iex
```

Follow the installation steps:
- Select the Databricks profile that you have just setup
- Install only for your tool of choice (e.g. if you're using Cursor, select Cursor)
- For installation scope, select `Project`. 

Once installation is complete, you should see MCP servers and Skills being added to your project directory

### Add Langchain MCP Server

Claude Code:
```
claude mcp add langchain-docs --transport http https://docs.langchain.com/mcp
```

Cursor:
Navigate to: Cursor -> Settings -> Cursor Settings -> Tools & MCP -> New MCP Server. 

Then add the following:
```
{
    "Docs by LangChain": {
        "name": "Docs by LangChain",
        "url": "https://docs.langchain.com/mcp",
        "headers": {}
    }
}
```

## Setting Up the Labs

### Setting Up Environment Variables
Create a `.env` file in the project root directory with the following content:

```
DATABRICKS_TOKEN=<databricks-personal-access-token>
DATABRICKS_HOST=https://<workspace-name>.cloud.databricks.com
MLFLOW_TRACKING_URI=databricks
MLFLOW_REGISTRY_URI=databricks-uc
MLFLOW_TRACING_SQL_WAREHOUSE_ID=<SQL_WAREHOUSE_ID>
MLFLOW_TRACING_DESTINATION=<catalog.schema> # Replace with your schema
```

### Creating Tables

In Claude/Cusor/Codex:
```
Use upload_to_volume to upload datasets from lab_setup/dataset to {catalog_name}.{schema_name} then use execute_sql to create a table for each of the dataset
```

Replace `catalog_name` and `schema_name` to your preferred catalog and schema

### Creating UC Function
In Claude/Cusor/Codex:
```
Use execute_sql to create the UC functions stored in lab_setup/scripts/uc_functions in {catalog_name}.{schema_name}
```

Replace `catalog_name` and `schema_name` to your preferred catalog and schema

### Creating MLflow Experiment
Before running the prompt below, ensure that the [OpenTelemetry on Databricks preview feature](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/trace-unity-catalog) is enabled in the workspace. 

In Claude/Cusor/Codex:
```
Use databricks-mlflow-setup to create a new mlflow experiment wtih traces to be stored in {catalog_name}.{schema_name}
```

Replace `catalog_name` and `schema_name` to your preferred catalog and schema