from threading import main_thread
from flask import Flask, render_template
main = Flask(__name__)
@main.route("/signin")
def sign_in():
 return render_template("signin.html")
@main.route('/signup')
def sign_up():
 return render_template("signup.html")
@main.route('/')
def home():
 return render_template("home.html")
@main.route('/about')
def about():
 return render_template("about.html")
if __name__ == '__main__':
    main.run(debug=True)