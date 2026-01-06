from google import genai

client = genai.Client(api_key="AIzaSyAQm_86X848rbDcGnfQc-1z4k8WFYcG39s")

with open("output_img.txt", "r", encoding="utf-8") as file:
    ocr_text = file.read()
prompt = f"""
Read the following lease contract text and extract these details clearly:

Interest Rate / APR:
Lease Duration:
Monthly Payment:
Down Payment:
Residual Value:
Mileage Allowance and Overage Charges:
Early Termination Clause:
Purchase Option (Buyout Price):
Maintenance Responsibilities:
Warranty and Insurance Coverage:
Penalties or Late Fee Clauses:

Contract Text:
{ocr_text}
"""
response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents=prompt
)

print("LLM Output:\n")
print(response.text)

with open("llm_output_img.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

print("\nLLM response saved successfully!")
