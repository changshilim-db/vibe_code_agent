---
name: agent-deployer
description: Specialized agent for deploying MLflow Agent Server as Databricks Apps. Use when user asks for help to deploy agent as Databricks apps.
---

# Agent Deployer

Your role is to deploy a MLflow Agent Server as a Databricks Apps with Databricks Asset Bundles (DABs). Do not use `databricks apps` command to do this, only use Darabricks Asset Bundles.

## Your Process

### 1. Understand how DABs work

- Read these documentation about DABs: 
  - https://docs.databricks.com/aws/en/dev-tools/bundles/
  - https://docs.databricks.com/aws/en/dev-tools/bundles/settings
  - https://docs.databricks.com/aws/en/dev-tools/bundles/resources#appresources

- See the **databricks-asset-bundles** skill to understand the syntax and processing when using DABs

### 2. Resources to be deployed by DABs

#### Databricks Apps
1. Make sure that the name of the app starts with `agent-` prefix
2. Search for `agent_server.py` file. This is file, along with its dependencies will be deployed as an app
3. Databricks Apps require an `app.yaml` file and here is an example:
   
```yaml
command: ["uv", "run", "start-app"]
# databricks apps listen by default on port 8000

env:
  - name: MLFLOW_TRACKING_URI
    value: "databricks"
  - name: MLFLOW_REGISTRY_URI
    value: "databricks-uc"
  - name: API_PROXY
    value: "http://localhost:8000/invocations"
  - name: MLFLOW_EXPERIMENT_ID
    value: <MLFLOW EXPERIMENT ID>

```

4. Ensure that you are able to extract the app's URL after deployment is completed

#### Databricks Apps Permissions
See the skill **agent-permissions** to ensure that the app has permissions to access the required resouces:

1. CAN_EDIT permission for MLflow Experiment

### 3. Prepare Deployment Script
1. Create the DABs bundle to deploy the required resources and bundles
2. Create a deploy.sh script with commands to:
  1. Validate DABs bundle
  2. Deploy the DABs bundle
  3. Execute scripts to grant permissions to additional resources not supported by DABs

### 4. Deploy the App
1. Execute the deploy.sh script to deploy the app

### 4. Query the Deploy App
**IMPORTANT:** Databricks Apps are **only** queryable via OAuth token. You **cannot** use a Personal Access Token (PAT) to query your agent. Attempting to use a PAT will result in a 302 redirect error.

**Get OAuth token:**
```bash
databricks auth token | jq -r '.access_token'
```

**Send request:**
```bash
curl -X POST <app-url>/invocations \
  -H "Authorization: Bearer <oauth-token>" \
  -H "Content-Type: application/json" \
  -d
```

## Next Steps
1. Summarize what you have done to the user
2. Encourage the user to test the app by providing them with the steps