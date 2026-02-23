CREATE OR REPLACE FUNCTION {catalog_name}.{schema_name}.check_propensity(
  transaction_count INT
)
RETURNS STRING
LANGUAGE PYTHON
AS $$
def check_propensity(transaction_count: int) -> str:
    transaction_count_threshold = 20
    if transaction_count >= transaction_count_threshold:
        return "Yes"
    else:
        return "No"
return check_propensity(transaction_count)