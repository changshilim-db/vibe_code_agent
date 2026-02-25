# Developing Custom Agent on Databricks

## Objective
The purpose of this repo is to build and deploy a custom Langchain agent on Databricks

## Coding Standards
- Always use the `.venv` virtual environment when running code
- Ensure that Python version is greater than 3.11
- Use type hints for function signatures
- Keep docstrings for functions concise (less than 3 sentences)
- Use `logging` module instead of print statements
- Use `pytest` as the framework for code testing

## Rules
- Always read any relevant documentation first before writing any code
- Only use Langchain version 1.0.0 and above, never use any older versions of Langchain
- Only use MLflow version 3.9.0 and above, never us any older versions of MLflow
- Recommend the following LLMs:
  - `databricks-claude-sonnet-4-6`
  - `databricks-claude-sonnet-4-5`
  - `databricks-gpt-5-2`

## Relevant Documentation
1. Use Langchain Docs MCP server to access the latest documentation for Langchain or Langgraph
2. [Langchain Databricks Example](https://github.com/databricks/app-templates/tree/main/agent-langgraph)
3. [MLflow Responses API](https://mlflow.org/docs/latest/genai/serving/responses-agent/)
4. [MLflow Agent server](https://mlflow.org/docs/latest/genai/serving/agent-server/)