# list of imports
from flask import Flask, render_template, request, send_file
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
from game_utils import gmail_create_draft
import os

app = Flask(__name__)

#secret key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


# all app routes
@app.route('/')
def index():
    return render_template("home/index.html")



@app.route('/contact')
def contact():
    return render_template("home/contact.html")

#biography app route
@app.route('/bio')
def biography():
    return render_template("home/bio.html")

#skills app route
@app.route('/skills')
def skills():
    return render_template("home/skills.html")

#cv app route
@app.route('/cv')
def download_cv():
    path = 'documents/royer-resume2023.pdf'
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)