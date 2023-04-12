from flask import Flask, render_template, request

app = Flask(__name__)

# set the DEBUG configuration option after creating the Flask app instance
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template("home/index.html")

@app.route('/contact')
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Do something with the form data (e.g. send an email)
        return 'Thank you for your message'
    else:
        # Display the contact form
        return render_template("home/contact.html")
    
@app.route('/bio')
def biography():
    return render_template("home/bio.html")

@app.route('/languages')
def languages():
    return render_template("home/languages.html")


if __name__ == "__main__":
    app.run()