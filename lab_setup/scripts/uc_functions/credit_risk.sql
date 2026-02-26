CREATE OR REPLACE FUNCTION {catalog_name}.{schema_name}.check_credit_risk (
  customer_id STRING COMMENT 'The customer ID'
)
RETURNS STRING
COMMENT 'Retrieves credit risk for a customer. Example usage: SELECT {{function_name}}("CUST0003")'
RETURN
  SELECT to_json(struct(customer_id, credit_score, risk_category, probability_of_default)) AS json_data
  FROM {catalog_name}.{schema_name}.apac_risk_profiles
  WHERE customer_id = customer_id
  LIMIT 1