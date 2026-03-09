---
name: agent-permissions
description: "Grant required permissions for agents in Databricks Asset Bundles in databricks.yml"
---

# Add Tools & Grant Permissions

**After adding any MCP server to your agent, you MUST grant the app access in `databricks.yml`.**

Without this, you'll get permission errors when the agent tries to use the resource.

## Workflow

**Step 1:** Grant access in `databricks.yml`:
```yaml
resources:
  apps:
    agent_langgraph:
      resources:
        - name: 'my_genie_space'
          genie_space:
            name: 'My Genie Space'
            space_id: '01234567-89ab-cdef'
            permission: 'CAN_RUN'
```

**Step 2:** Deploy and run:
```bash
databricks bundle deploy
databricks bundle run agent_langgraph  # Required to start app with new code!
```

## Resource Type Examples

See the `examples/` directory for complete YAML snippets:

| File | Resource Type | When to Use |
|------|--------------|-------------|
| `uc-function.yaml` | Unity Catalog function | UC functions via MCP |
| `uc-table.yaml` | Unity Catalog Table | UC table |
| `uc-connection.yaml` | UC connection | External MCP servers |
| `vector-search.yaml` | Vector search index | RAG applications |
| `sql-warehouse.yaml` | SQL warehouse | SQL execution |
| `serving-endpoint.yaml` | Model serving endpoint | Model inference |
| `genie-space.yaml` | Genie space | Natural language data |
| `lakebase.yaml` | Lakebase database | Agent memory storage |
| `experiment.yaml` | MLflow experiment | Tracing (already configured) |
| `custom-mcp-server.md` | Custom MCP apps | Apps starting with `mcp-*` |

See `examples/custom-mcp-server.md` for detailed steps.

## valueFrom Pattern (for app.yaml)

**IMPORTANT**: Make sure all `valueFrom` references in `app.yaml` reference an existing key in the `databricks.yml` file. 
Some resources need environment variables in your app. Use `valueFrom` in `app.yaml` to reference resources defined in `databricks.yml`:

```yaml
# app.yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: "experiment"        # References resources.apps.<app>.resources[name='experiment']
  - name: LAKEBASE_INSTANCE_NAME
    valueFrom: "database"   # References resources.apps.<app>.resources[name='database']
```

**Critical:** Every `valueFrom` value must match a `name` field in `databricks.yml` resources.

## Important Notes

- **Multiple resources**: Add multiple entries under `resources:` list
- **Permission types vary**: Each resource type has specific permission values
- **Deploy + Run after changes**: Run both `databricks bundle deploy` AND `databricks bundle run agent_langgraph`
- **valueFrom matching**: Ensure `app.yaml` `valueFrom` values match `databricks.yml` resource `name` values
