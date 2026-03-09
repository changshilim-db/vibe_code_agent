# Get Started

## Installation
First, we’ll need to set up a Python environment and install a few MCP servers and skills. To ensure the best experience during these labs, we recommend disabling any MCP servers or skills you may have previously configured.

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

### Additional Scripts to Run

<details>
<summary>For Cursor Only</summary>

Rename the `.claude` folder to `.cursor`.

</details>

<details>
<summary>For Codex Only</summary>

Run the following script to copy files over to `.agents` folder:

```bash
python lab_setup/scripts/initialization/setup_codex.py
 ```

</details>

### Setup Databricks Locally

#### Databricks CLI
Ensure that you have the latest version of Databricks CLI install. Refer to this [documentation](https://docs.databricks.com/aws/en/dev-tools/cli/install) for more details

#### Setup Databricks Profile 
Run the following command to authenticate and set up a Databricks Profile for your workspace:
```
databricks auth login <workspace-url>
```

### Installing AI Tool Kits

#### Install ai-dev-kit
Install [ai-dev-kit](https://github.com/databricks-solutions/ai-dev-kit/tree/main) by running the following command in the project directory:

<details>
<summary>Mac user:</summary>

```
bash <(curl -sL https://raw.githubusercontent.com/databricks-solutions/ai-dev-kit/main/install.sh)
```

</details>

<details>
<summary>Windows user:</summary>

```
irm https://raw.githubusercontent.com/databricks-solutions/ai-dev-kit/main/install.ps1 | iex
```

</details>

Follow the installation steps:
- Select the Databricks profile that you have just setup
- Install only for your tool of choice (e.g. if you're using Cursor, select Cursor)
- For installation scope, select `Project`. 

Once installation is complete, you should see MCP servers and Skills being added to your project directory

#### Add Langchain MCP Server

<details>
<summary>Claude Code:</summary>

```
claude mcp add langchain-docs --transport http https://docs.langchain.com/mcp
```

</details>

<details>
<summary>Cursor:</summary>

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

</details>

<details>
<summary>Codex:</summary>

The MCP server is already added in the [project's codex's file](../.codex/config.toml)

Send the following prompt to check that the MCP server is properly configured:

```
Search langchain docs and explain what is create_agent
```

</details>

## Setting Up the Labs

**Note: Before proceeding, you may need to restart your IDE or Claude Code session so the installed skills and MCP servers are detected**

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

Refer to this documentation on how to [create a personal access token](https://docs.databricks.com/aws/en/dev-tools/auth/pat#create-personal-access-tokens-for-workspace-users)

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
Use databricks-mlflow-setup to create a new mlflow experiment
```

Replace `catalog_name` and `schema_name` to your preferred catalog and schema