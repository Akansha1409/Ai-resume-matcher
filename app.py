import streamlit as st
import os
from groq import Groq
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

# Load environment variables from a .env file (for local dev)
load_dotenv()

# --- Page Config ---
st.set_page_config(page_title="AI Resume Matcher", page_icon="🎯", layout="wide")

# Initialize Groq Client
# It will look for 'GROQ_API_KEY' in your environment variables
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

def extract_text_from_pdf(file):
    """Extracts all text from an uploaded PDF file."""
    try:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

def calculate_match_score(resume_text, job_desc):
    """Calculates TF-IDF Cosine Similarity score."""
    documents = [resume_text, job_desc]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    # Compare the first document (Resume) with the second (Job Desc)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(float(similarity[0][0]) * 100, 2)

# --- UI Header ---
st.title("🎯 AI-Powered Resume-to-Job Matcher")
st.markdown("---")

# Error check for API Key
if not api_key:
    st.warning("⚠️ GROQ_API_KEY not found! Please set it in your environment variables or .env file.")

# --- Layout ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📁 Step 1: Upload Resume")
    uploaded_file = st.file_uploader("Upload your Resume in PDF format", type="pdf")
    
    st.subheader("📝 Step 2: Paste Job Description")
    job_description = st.text_area("Paste the target job description here...", height=300)

with col2:
    st.subheader("📊 Step 3: Analysis & Results")
    
    if st.button("Analyze Match"):
        if uploaded_file and job_description:
            with st.spinner("Processing..."):
                # 1. Extraction
                resume_text = extract_text_from_pdf(uploaded_file)
                
                if not resume_text.strip():
                    st.error("Could not extract text from the PDF. Please check the file.")
                else:
                    # 2. Traditional ML Scoring
                    score = calculate_match_score(resume_text, job_description)
                    
                    # 3. Visual Score Display
                    st.write(f"### Current Match Score: **{score}%**")
                    st.progress(score / 100)
                    
                    # 4. Generative AI Feedback (Groq)
                    if client:
                        prompt = f"""
                        Analyze the following Resume against the Job Description.
                        Resume Content: {resume_text[:3000]}
                        Job Description: {job_description[:3000]}
                        
                        The TF-IDF similarity score is {score}%. 
                        
                        Provide:
                        1. A list of 5 key missing keywords/skills from the resume.
                        2. Three actionable bullet points to improve the resume specifically for this job description.
                        3. A final 'Verdict' on whether the candidate is a strong fit.
                        
                        Format the output using professional markdown.
                        """
                        
                        try:
                            response = client.chat.completions.create(
                                model="llama-3.3-70b-versatile",
                                messages=[{"role": "user", "content": prompt}],
                                temperature=0.5,
                            )
                            st.markdown("### 🤖 AI Optimization Tips")
                            st.write(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"AI Feedback Error: {e}")
        else:
            st.info("Please provide both a Resume and a Job Description to begin.")

# --- Footer ---
st.markdown("---")
st.caption("Powered by Llama 3.3 via Groq | Built with Streamlit & Scikit-learn")