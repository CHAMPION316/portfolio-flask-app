# list of imports
from flask import Flask, render_template, request, send_file
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
import os

app = Flask(__name__)

#secret key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# set the DEBUG configuration option after creating the Flask app instance
# app.config['DEBUG'] = True

# app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
# app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
# app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS,') == 'False'
# app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL,') == 'True'
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME'), 
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

# mail = Mail(app)

# all app routes
@app.route('/')
def index():
    return render_template("home/index.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        sender_name = request.form['name']
        sender_email = request.form['email']
        recipient_email = "royer.seguracalderon@gmail.com"
        subject = "Programmer job opportunity {}".format(sender_name)
        message = request.form['message']
        
        msg = EmailMessage()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.set_content(message)
        
        #SMTP Configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = os.environ.get('MAIL_USERNAME')
        smtp_password = os.environ.get('MAIL_PASSWORD')        
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.send_message(msg)
                
            return 'Email sent successfully!'
        except smtplib.SMTPException as e:
            return 'Error occurred while sending mail: {}'.format(str(e))
        
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