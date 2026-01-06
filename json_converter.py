import json
import re
with open("llm_output_img.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

def extract_percentage(text):
    match = re.search(r"(\d+(\.\d+)?\s*%)", text)
    return match.group(1) if match else None

def extract_money(text):
    match = re.search(r"(₹\s?\d+[,\d]*)", text)
    return match.group(1) if match else None

def extract_duration(text):
    match = re.search(r"(\d+\s*(months|month|years|year))", text)
    return match.group(1) if match else None

def extract_sentence(keyword):
    match = re.search(rf"{keyword}.*", text)
    return match.group(0) if match else None


sla_data = {
    "interest_rate_apr": extract_percentage(text),
    "lease_term_duration": extract_duration(text),
    "monthly_payment": extract_money(text),
    "down_payment": extract_money(text),
    "residual_value": extract_money(text),
    "mileage_allowance_and_overage_charges": extract_sentence("mileage"),
    "early_termination_clause": extract_sentence("termination"),
    "purchase_option_buyout_price": extract_money(text),
    "maintenance_responsibilities": extract_sentence("maintenance"),
    "warranty_and_insurance_coverage": extract_sentence("warranty"),
    "penalties_or_late_fee_clauses": extract_sentence("penalty")
}

with open("sla_extracted.json", "w", encoding="utf-8") as file:
    json.dump(sla_data, file, indent=4)

print("SLA JSON extracted successfully.")
