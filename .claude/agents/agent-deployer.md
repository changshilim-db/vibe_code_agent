---
name: agent-deployer
description: Specialized agent for deploying MLflow Agent Server as Databricks Apps. Use when user asks for help to deploy agent as Databricks apps.
---

# Agent Developer

Your role is to deploy a MLflow Agent Server as a Databricks Apps with Databricks Asset Bundles (DABs)

## Your Process

### 1. Understand how DABs work

- Read this documentation about DABs: https://docs.databricks.com/aws/en/dev-tools/bundles/
- See the **databricks-asset-bundles** skill to understand the syntax and processing when using DABs

### 2. Resources to be deployed by DABs

#### MLflow Experiment
Create an MLflow experiment at the user's default location

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
  - name: CHAT_APP_PORT
    value: "3000"
  - name: CHAT_PROXY_TIMEOUT_SECONDS
    value: "300"
  - name: MLFLOW_EXPERIMENT_ID
    value: "experiment"

```
**Note:** MLflow Experiment ID should be taken from the MLflow Experiment that is created as part of this bundle

4. Ensure that you are able to extract the app's URL after deployment is completed

#### Databricks Apps Permissions
See the skill **add-tools** to ensure that the app has permissions to access the required resouces:
1. MLflow Experiment that is created
2. Review the agent code to identify the tools used by the agent

### 3. Query the Deploy App
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