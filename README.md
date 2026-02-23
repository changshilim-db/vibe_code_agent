# Databricks Agent Vibe Coding Workshop

## Overview
This repository contains materials to vibe code an Agent on Databricks

## Get Started
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

Follow the installation steps. For installation scope, select `Project`. 

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

### Uploading Dataset

In Claude/Cusor:
```
Use upload_to_volume to upload datasets from lab_setup/dataset to {catalog_name}.{schema_name} then use execute_sql to create a table for each of the dataset
```

Replace `catalog_name` and `schema_name` to your preferred catalog and schema

### Creating UC Function
```
Use execute_sql to create the UC functions stored in lab_setup/scripts/uc_functions in {catalog_name}.{schema_name}
```

Replace `catalog_name` and `schema_name` to your preferred catalog and schema