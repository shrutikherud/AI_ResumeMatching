[![HTML5](https://img.shields.io/badge/html5-E34F26.svg?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS3](https://img.shields.io/badge/css3-1572B6.svg?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/bootstrap-7952B3.svg?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![JavaScript](https://img.shields.io/badge/javascript-F7DF1E.svg?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Python](https://img.shields.io/badge/python-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-000000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![NLP](https://img.shields.io/badge/NLP-4B8BBE.svg?style=flat&logo=spacy&logoColor=white)](https://en.wikipedia.org/wiki/Natural_language_processing)


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
