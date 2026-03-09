---
name: databricks-langchain
description: "Integration between langchain and Databricks. Use when user wants to integrate Databricks LLM, Embeddings, Vector Store or MCP with Langchain"
---

# Databricks Langchain

## SDK Setup

```python
import mlflow
from databricks.sdk import WorkspaceClient
from databricks_langchain import ChatDatabricks, DatabricksMCPServer, DatabricksMultiServerMCPClient
from langchain.agents import create_agent

# Add at the beginning of the scrip to enable autologging for tracing
mlflow.langchain.autolog()

# Initialize workspace client
workspace_client = WorkspaceClient()
```

---

## databricks-langchain SDK Overview

**SDK Location:** https://github.com/databricks/databricks-ai-bridge/tree/main/integrations/langchain

Before making any changes, ensure that the APIs actually exist in the SDK. If something is missing from the documentation here, look in the venv's `site-packages` directory for the `databricks_langchain` package.

---

### ChatDatabricks - LLM Chat Interface

Connects to Databricks Model Serving endpoints for LLM inference.

```python
from databricks_langchain import ChatDatabricks

llm = ChatDatabricks(
    endpoint="databricks-claude-4-5-sonnet"
)

# For Responses API agents:
llm = ChatDatabricks(endpoint="my-agent-endpoint", use_responses_api=True)
```

Available models (check workspace for current list):
- `databricks-claude-sonnet-4-5`
- `databricks-gpt-5-2`

---

### DatabricksEmbeddings - Generate Embeddings

Query Databricks embedding model endpoints.

```python
from databricks_langchain import DatabricksEmbeddings

embeddings = DatabricksEmbeddings(endpoint="databricks-qwen3-embedding-0-6b")
vector = embeddings.embed_query("The meaning of life is 42")
vectors = embeddings.embed_documents(["doc1", "doc2"])
```

---

### DatabricksVectorSearch - Vector Store

Connect to Databricks Vector Search indexes for similarity search.

```python
from databricks_langchain import DatabricksVectorSearch

# Delta-sync index with Databricks-managed embeddings
vs = DatabricksVectorSearch(index_name="catalog.schema.index_name")

# Direct-access or self-managed embeddings
vs = DatabricksVectorSearch(
    index_name="catalog.schema.index_name",
    embedding=embeddings,
    text_column="content",
)

docs = vs.similarity_search("query", k=5)
```

---

### MCP Client - Tool Integration

Connect to MCP (Model Context Protocol) servers to get tools for your agent.

**Basic MCP Server (manual URL):**

```python
from databricks_langchain import DatabricksMCPServer, DatabricksMultiServerMCPClient

client = DatabricksMultiServerMCPClient([
    DatabricksMCPServer(
        name="system-ai",
        url=f"{host}/api/2.0/mcp/functions/system/ai",
    )
])
tools = await client.get_tools()
```

**From UC Function (convenience helper):**

Creates MCP server for Unity Catalog functions. If `function_name` is omitted, exposes all functions in the schema.

```python
server = DatabricksMCPServer.from_uc_function(
    catalog="main",
    schema="tools",
    function_name="send_email",  # Optional - omit for all functions in schema
    name="email-server",
    timeout=30.0,
    handle_tool_error=True,
)
```

**From Vector Search (convenience helper):**

Creates MCP server for Vector Search indexes. If `index_name` is omitted, exposes all indexes in the schema.

```python
server = DatabricksMCPServer.from_vector_search(
    catalog="main",
    schema="embeddings",
    index_name="product_docs",  # Optional - omit for all indexes in schema
    name="docs-search",
    timeout=30.0,
)
```

**From Genie Space:**

Create MCP server from Genie Space. Get the genie space ID from the URL.

Example: `https://workspace.cloud.databricks.com/genie/rooms/01f0515f6739169283ef2c39b7329700?o=123` means the genie space ID is `01f0515f6739169283ef2c39b7329700`

```python
DatabricksMCPServer(
    name="genie",
    url=f"{host_name}/api/2.0/mcp/genie/01f0515f6739169283ef2c39b7329700",
)
```

**Non-Databricks MCP Server:**

```python
from databricks_langchain import MCPServer

server = MCPServer(
    name="external-server",
    url="https://other-server.com/mcp",
    headers={"X-API-Key": "secret"},
    timeout=15.0,
)
```

---

## External Resources

1. [databricks-langchain SDK](https://github.com/databricks/databricks-ai-bridge/tree/main/integrations/langchain)
2. [Langchain Databricks Example](https://github.com/databricks/app-templates/tree/main/agent-langgraph)
3. [Adding tools](https://docs.databricks.com/aws/en/generative-ai/agent-framework/agent-tool)
4. [LangGraph documentation](https://docs.langchain.com/oss/python/langgraph/overview)
5. [Responses API](https://mlflow.org/docs/latest/genai/serving/responses-agent/)

