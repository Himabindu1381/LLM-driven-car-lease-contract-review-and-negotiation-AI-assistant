import json
from google import genai

client = genai.Client(
    api_key="AIzaSyBQBEeJF9See34ZpwSnaE--hGOxdF_cyHc"
)

def extract_sla_llm(text: str):
    prompt = f"""
Extract ONLY the following fields from the document.

STRICT RULES:
- Return ONLY valid JSON
- NO explanations
- NO sentences
- NO extra text
- If a value is not found, return an empty string ""
- Use EXACT field names given below
- Do NOT add or remove fields

JSON FORMAT (EXACT):
{{
  "interest_rate_apr": "",
  "lease_term_duration": "",
  "monthly_payment": "",
  "down_payment": "",
  "residual_value": "",
  "mileage_allowance_and_overage_charges": "",
  "early_termination_clause": "",
  "purchase_option_buyout_price": "",
  "maintenance_responsibilities": "",
  "warranty_and_insurance_coverage": "",
  "penalties_or_late_fee_clauses": ""
}}

DOCUMENT TEXT:
{text}
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    output = response.text.strip()

    if not output:
        raise ValueError("LLM returned empty response")

    return json.loads(output)
