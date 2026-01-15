from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import traceback

from ocr import extract_text
from llm_service import extract_sla_llm
from fairness_service import calculate_fairness

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract-sla")
async def extract_sla(file: UploadFile = File(...)):
    try:
        # 1. OCR
        extracted_text = extract_text(file)

        # 2. SLA extraction
        sla_data = extract_sla_llm(extracted_text)

        # 3. Fairness analysis
        fairness_result = calculate_fairness(sla_data)

        return {
            "status": "success",
            "sla_data": sla_data,
            "fairness_score": fairness_result["fairness_score"],
            "fairness_level": fairness_result["fairness_level"],
            "red_flags": fairness_result["red_flags"]
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "traceback": traceback.format_exc()
        }
