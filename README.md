# JobFitAI - Smart Resume Matcher

A smart resume screening tool that uses AI and NLP to match candidates with job descriptions. It automates shortlisting, identifies skill gaps, making hiring faster and more accurate for recruiters and job seekers alike.

&nbsp;
## 🚀 Features

- **Multi-Format Support**: Processes PDF, DOCX, and TXT resume formats
- **Intelligent Matching**: Uses TF-IDF vectorization and cosine similarity to rank resumes
- **Skill Gap Analysis**: Identifies missing skills from job requirements
- **Top Candidate Highlighting**: Visually distinguishes top 3 matches with ranking badges
- **PDF Report Generation**: Download comprehensive matching results as PDF

&nbsp;
## 🧱 Tech Stack

| Layer           | Technology                                               |
|------------------|----------------------------------------------------------|
| Frontend         | HTML5, CSS3, Bootstrap 5, JavaScript                     |
| Web Framework    | Flask (Python)                                           |
| Text Processing  | PyPDF2, docx2txt, re                                     |
| NLP & Matching   | scikit-learn (TF-IDF, Cosine Similarity)                 |
| PDF Generation   | ReportLab                                                |

&nbsp;
## ⚙️ How It Works

1. **Text Extraction**: Uses PyPDF2 and docx2txt to extract text from resumes
2. **Preprocessing**: Cleans and normalizes text (lowercasing, stopword removal)
3. **Matching Algorithm**:
   - TF-IDF vectorization of job description and resumes
   - Cosine similarity scoring
4. **Skills Analysis**:
   - Extracts skills from both job description and resumes
   - Compares to identify missing skills
5. **Results Display**:
   - Ranks candidates by match percentage
   - Highlights top 3 candidates
   - Shows missing skills for each candidate

&nbsp;
## 🧠 Future Enhancements

- Job portal integration
- ATS-friendly resume scoring
- AI-based job recommendations
- Modern UI with React or Streamlit
