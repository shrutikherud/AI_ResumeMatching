from flask import Flask, request, render_template, make_response
import PyPDF2
import docx2txt
import os
import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Skill database - minimal version
SKILLS_DB = [
    'python', 'java', 'sql', 'machine learning', 'aws',
    'flask', 'django', 'c++', 'javascript', 'communication',
    'leadership', 'teamwork', 'problem solving'
]


def extract_skills(text):
    text = text.lower()
    skills_found = set()
    for skill in SKILLS_DB:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            skills_found.add(skill)
    return list(skills_found)


def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)


def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        return file.read()


def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    elif file_path.endswith(".txt"):
        return extract_text_from_txt(file_path)
    else:
        return ""


@app.route("/")
def matchresume():
    return render_template('matchresume.html')


@app.route("/matcher", methods=['GET', 'POST'])
def matcher():
    if request.method == 'POST':
        job_description = request.form.get('job_description')
        resume_files = request.files.getlist('resumes')

        resumes = []
        for resume_file in resume_files:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(filename)
            resumes.append(extract_text(filename))

        if not resumes or not job_description:
            return render_template('matchresume.html', message="Please Upload resumes and post job")

        jd_skills = extract_skills(job_description)

        vectorizer = TfidfVectorizer().fit_transform([job_description] + resumes)
        vectors = vectorizer.toarray()

        job_vector = vectors[0]
        resume_vectors = vectors[1:]

        similarities = cosine_similarity([job_vector], resume_vectors)[0]

        results = []
        for i, resume_text in enumerate(resumes):
            resume_skills = extract_skills(resume_text)
            missing_skills = list(set(jd_skills) - set(resume_skills))

            results.append({
                'filename': resume_files[i].filename,
                'score': round(similarities[i] * 100, 2),
                'missing_skills': missing_skills[:5]
            })

        results.sort(key=lambda x: x['score'], reverse=True)

        return render_template('matchresume.html',
                               message="Top matching resumes",
                               results=results,
                               job_description=job_description)

    return render_template('matchresume.html')


@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    try:
        results_data = request.form.get('results_data')
        job_description = request.form.get('job_description', '')

        if not results_data:
            return "No results data provided", 400

        results = json.loads(results_data)
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 750, "Resume Matching Results Report")

        p.setFont("Helvetica-Bold", 12)
        p.drawString(100, 720, "Job Description:")
        y_position = 700

        # Clean the job description text
        clean_jd = ''.join([c if ord(c) < 128 else ' ' for c in job_description])
        lines = clean_jd.split('\n')

        p.setFont("Helvetica", 10)
        for line in lines:
            if y_position < 100:
                p.showPage()
                y_position = 750
                p.setFont("Helvetica-Bold", 12)
                p.drawString(100, y_position, "Job Description (continued):")
                y_position -= 20
                p.setFont("Helvetica", 10)

            p.drawString(100, y_position, line.strip())
            y_position -= 15
            if not line.strip():
                y_position -= 5

        y_position -= 20

        p.setFont("Helvetica-Bold", 14)
        p.drawString(100, y_position, "Matching Results:")
        y_position -= 30

        for idx, result in enumerate(results):
            if y_position < 100:
                p.showPage()
                y_position = 750
                p.setFont("Helvetica-Bold", 14)
                p.drawString(100, y_position, "Matching Results (continued):")
                y_position -= 30

            p.setFont("Helvetica-Bold", 14)
            rank_tag = ""
            if idx == 0:
                rank_tag = " (TOP 1)"
            elif idx == 1:
                rank_tag = " (TOP 2)"
            elif idx == 2:
                rank_tag = " (TOP 3)"

            p.drawString(100, y_position, f"Resume: {result['filename']}{rank_tag}")
            y_position -= 20

            p.setFont("Helvetica", 10)
            p.drawString(100, y_position, f"Match Score: {result['score']}%")
            y_position -= 15

            if result.get('missing_skills'):
                p.drawString(100, y_position, "Missing Skills:")
                y_position -= 15
                skills = ", ".join(result['missing_skills'])
                p.drawString(120, y_position, skills)
                y_position -= 20
            else:
                p.drawString(100, y_position, "No missing skills identified")
                y_position -= 20

            y_position -= 10

        p.save()
        buffer.seek(0)

        response = make_response(buffer.getvalue())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=resume_matching_results.pdf'
        return response

    except Exception as e:
        app.logger.error(f"Error generating PDF: {str(e)}")
        return f"Error generating PDF: {str(e)}", 500


if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)