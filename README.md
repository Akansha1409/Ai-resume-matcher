# 🤖 AI Resume Matcher & Career Optimizer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-f55036?style=for-the-badge&logo=lightning&logoColor=white" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
</p>

### 🚀 [Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/ak1409/ai-resume)

An intelligent **Applicant Tracking System (ATS)** analyzer that bridges the gap between job seekers and recruiters. Leveraging the lightning-fast **Llama 3.3 (70B)** model via Groq, this tool provides deep semantic analysis, keyword gap identification, and actionable feedback to optimize your resume for specific job descriptions.

---

## ✨ Key Features

- **🎯 Semantic Scoring:** Uses Cosine Similarity and LLMs to go beyond simple keyword counting.
- **🔍 Gap Analysis:** Identifies missing hard skills, certifications, and technical keywords.
- **💡 Actionable Insights:** Provides 3-5 specific bullet points to improve your resume's impact.
- **⚡ High Performance:** Near-instant results powered by Groq's LPU™ Inference Engine.
- **📂 PDF Support:** Seamless text extraction from multi-page PDF resumes.

---

## 🛠️ Technical Stack

- **AI Model:** Llama 3.3-70b-versatile (via Groq Cloud API)
- **Framework:** Streamlit (Web UI)
- **Text Processing:** PyPDF2 (Extraction) & Scikit-learn (TF-IDF Vectorization)
- **Deployment:** Hugging Face Spaces / GitHub

---

## 📂 Project Structure

```text
AI-Resume-Matcher/
├── app.py              # Main Streamlit application logic
├── requirements.txt    # Production dependencies
├── .env                # API Keys (Local use only - Git ignored)
└── README.md           # Documentation
```

---

## 📊 How It Works

> ### 1. Text Extraction
> The tool parses the uploaded PDF using `PyPDF2` to transform unstructured document data into clean text for analysis.

> ### 2. Vectorization
> It creates a mathematical representation of both the Resume and the JD using `TF-IDF` vectorization, focusing on keyword density and importance.

> ### 3. Similarity Analysis
> A mathematical base score is calculated using `Cosine Similarity` to determine the initial alignment between the candidate and the role.

> ### 4. LLM Refinement
> The text is sent to the **Llama 3.3** model via Groq to provide a qualitative, human-like critique of the candidate's fit and actionable optimization tips.
