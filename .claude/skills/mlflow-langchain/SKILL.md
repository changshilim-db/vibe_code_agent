---
name: mlflow-langchain
description: "Integration between MLflow and Langchain/Langgraph. Use when user wants wrap Langchain/Langgraph code with MLflow"
---

# MLflow Langchain

## Tracing

The following command will help in instrumenting auto-tracing
```python
mlflow.langchain.autolog()
```

## Handling Langchain Agent Outputs

#### Streaming

```python
@stream()
async def streaming(request: ResponsesAgentRequest) -> AsyncGenerator[ResponsesAgentStreamEvent, None]:
    agent = await init_agent() #initialize langchain agent

    user_messages = to_chat_completions_input([i.model_dump() for i in request.input])
    messages = {"messages": user_messages}

    async for event in process_agent_astream_events(
        agent.astream(messages, stream_mode=["updates", "messages"])
    ):
        yield event
```

See [examples/utils.py](examples/utils.py) on how to implement `process_agent_astream_events`

#### Non-Streaming

```python
@invoke()
async def non_streaming(request: ResponsesAgentRequest) -> ResponsesAgentResponse:
    outputs = [
        event.item
        async for event in streaming(request)
        if event.type == "response.output_item.done"
    ]
    return ResponsesAgentResponse(output=outputs)
```

## MLflow Agent Server

### Agent Server Setup
Place Langchain/Langgraph Code, along with the `@invoke()` and `@streaming()` functions in the same file (e.g. `agent.py`)

Then wrap it with MLflow Agent Server, create an `agent_server.py` file:

```python
from mlflow.genai.agent_server import AgentServer, setup_mlflow_git_based_version_tracking

# Need to import the agent to register the functions with the server
import agent  # change to file name of agent code

agent_server = AgentServer("ResponsesAgent", enable_chat_proxy=True)

# Define the app as a module level variable to enable multiple workers
app = agent_server.app  # noqa: F841
setup_mlflow_git_based_version_tracking()


def main():
    agent_server.run(app_import_string="agent_server:app")
```

### Example Input

query_input = {
    "input": [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "i am good"}
    ],
}

## Useful Resources
1. [Agent server](https://mlflow.org/docs/latest/genai/serving/agent-server/)
2. [Responses API](https://mlflow.org/docs/latest/genai/serving/responses-agent/)