# Walkthrough

## 1.0 Develop a LangChain Agent Locally
Create a LangChain agent integrated with MLflow. Use the `agent-developer` subagent to help us with this.

Helper prompt:
```text
Use agent-developer to help me create a LangChain agent.
```

The subagent will ask a few follow-up questions (for example, which LLM and which tools to use).

Helper prompt:
```
For the LLM, use databricks-claude-sonnet-4-5. The agent must integrate with UC functions in <catalog_name>.<schema_name>.

The agent needs to answer questions about banking customers.
```

The subagent will reference LangChain, Databricks, and MLflow documentation to implement the agent. By the end of this step, the coding assistant should have:
1. Created a LangChain agent
2. Integrated the agent with MLflow (wrapping it as an MLflow Agent Server)
3. Added basic test scripts to validate functionality

**Note:** At this stage, you don’t need to validate answer quality or accuracy—we’ll focus on correctness and runtime behavior first.

## 2.0 Test the Agent Locally
Once the agent code is complete, run local tests to confirm everything works end-to-end, including the MLflow Agent Server.

Helper prompt:
```
Please test the agent code and the MLflow Agent Server locally.
```

The coding assistant should run the tests, fix issues as needed, start the MLflow Agent Server on localhost, and send a few sample requests.

By the end of this step, confirm that:
1. The agent correctly calls the UC functions you created
2. The MLflow Agent Server runs without errors
3. Traces appear in the associated MLflow experiment

## 3.0 Deploy the Agent as a Databricks App
After the MLflow Agent Server works locally, deploy it as a Databricks App using the agent-deployer subagent.

Helper prompt:
```
Use agent-deployer to help deploy the agent as a Databricks App.
```

The `agent-deployer` subagent will use Databricks Asset Bundles (DABs) to package and deploy the app. After deployment, the coding assistant should query the app endpoint with a few requests.

By the end of this step, confirm that:
1. The agent is successfully deployed as a Databricks App
2. Traces are visible in the MLflow experiment

### 4.0 Monitor Agent Performance
After deployment, monitor performance using the agent-trace-analyzer to analyze traces and build an AI/BI dashboard.

Helper prompt:
```
/agent-trace-analyzer help me monitor the agent’s performance with a dashboard. The agent traces are stored in <catalog_name>.<schema_name>
```

By the end of this step, confirm that:
1. A dashboard is created to monitor agent traces over time