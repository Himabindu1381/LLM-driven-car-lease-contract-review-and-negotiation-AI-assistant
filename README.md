# LLM-Driven Car Lease Contract Review & Negotiation Assistant 🚗📄

This project is an AI-powered backend system that helps users **analyze car lease and loan agreements** by extracting text from documents and using **Large Language Models (LLMs)** to provide insights such as fairness checks, summaries, and structured outputs.

The backend has been **refactored using FastAPI** to ensure better performance, scalability, and clean API design.

---

## 🚀 Features

- 📄 **PDF & Document OCR**
  - Extracts text from car lease/loan agreements.
- 🤖 **LLM-based Analysis**
  - Reviews contracts and highlights important clauses.
- ⚖️ **Fairness Evaluation**
  - Identifies potentially unfair or risky terms.
- 🧠 **Modular Backend Design**
  - Separate services for OCR, LLM processing, and fairness logic.
- ⚡ **FastAPI Framework**
  - High-performance, async-ready REST APIs.

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI  
- **Language:** Python  
- **OCR:** Python-based OCR utilities  
- **AI/LLM:** LLM service integration  
- **API Server:** Uvicorn  

---

## 📂 Project Structure

├── main.py # FastAPI entry point
├── ocr.py # OCR logic for documents
├── llm_service.py # LLM integration and processing
├── fairness_service.py # Contract fairness analysis
├── uploads/ # Uploaded documents
├── requirements.txt # Project dependencies
├── .gitignore
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Himabindu1381/LLM-driven-car-lease-contract-review-and-negotiation-AI-assistant.git
   cd LLM-driven-car-lease-contract-review-and-negotiation-AI-assistant
Create a virtual environment

bash
Copy code
python -m venv .venv
Activate the virtual environment

Windows:

bash
Copy code
.venv\Scripts\activate
macOS/Linux:

bash
Copy code
source .venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
▶️ Running the Application
Start the FastAPI server using:

bash
Copy code
uvicorn main:app --reload
API will be available at:
👉 http://127.0.0.1:8000

Swagger UI (API docs):
👉 http://127.0.0.1:8000/docs

🔄 Project Update
This project was initially developed with a basic backend structure and has been refactored to FastAPI for improved scalability, modularity, and performance.

📌 Future Enhancements
Advanced clause-level negotiation suggestions

Multi-language document support

Frontend integration

Deployment on cloud platforms

👩‍💻 Author
Himabindu Donikena
B.Tech Student | Backend & AI Enthusiast
