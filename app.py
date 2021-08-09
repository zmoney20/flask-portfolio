from flask import Flask, render_template
from static.data import project_data
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', len=len(project_data), project_data=project_data)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)