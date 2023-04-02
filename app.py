from flask import Flask, render_template, request

app = Flask(__name__)

# set the DEBUG configuration option after creating the Flask app instance
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact/contact.html")

if __name__ == "__main__":
    app.run()