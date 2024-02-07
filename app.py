from flask import Flask, render_template
from router.oauth import oauth

app = Flask(__name__)
app.register_blueprint(oauth)
app.secret_key = 'your_secret_key_here'

@app.route("/login")
def login():
    return render_template('home.html')

@app.route("/", methods=['POST'])
def home():
    return "do this"

    


    



