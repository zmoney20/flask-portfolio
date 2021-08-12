from flask import Flask, render_template
from static.data import project_data, work_data, education_data, skills

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
            'home.html',
            len_project=len(project_data),
            project_data=project_data,
            len_education=len(education_data),
            education_data=education_data,
            len_work=len(work_data),
            work_data=work_data,
            )

@app.route("/about")
def about():
    return render_template(
            'about.html',
            len_skills=len(skills),
            skills=skills
            )

if __name__ == '__main__':
    app.run(debug=True)
